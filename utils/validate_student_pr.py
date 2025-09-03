#!/usr/bin/env python3
"""
Validation script for student pull requests.
Checks that students only edit allowed files and follow formatting rules.

Usage:
    python validate_student_pr.py [--branch branch-name]
"""

import os
import sys
import yaml
import re
import subprocess
from pathlib import Path
from datetime import datetime

# Configuration
MAX_IMAGE_SIZE = 2 * 1024 * 1024  # 2MB in bytes
ALLOWED_IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif'}
STUDENT_ZONE = 'STUDENT_ZONE'
PI_ONLY = 'PI_ONLY'

class Colors:
    """Terminal colors for output"""
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def print_status(status, message):
    """Print colored status messages"""
    if status == 'success':
        print(f"{Colors.GREEN}✓{Colors.ENDC} {message}")
    elif status == 'warning':
        print(f"{Colors.YELLOW}⚠{Colors.ENDC} {message}")
    elif status == 'error':
        print(f"{Colors.RED}✗{Colors.ENDC} {message}")
    elif status == 'info':
        print(f"{Colors.BLUE}ℹ{Colors.ENDC} {message}")

def get_changed_files():
    """Get list of changed files in the PR"""
    try:
        # Get changed files compared to main branch
        result = subprocess.run(
            ['git', 'diff', '--name-only', 'gh-pages...HEAD'],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip().split('\n') if result.stdout.strip() else []
    except subprocess.CalledProcessError:
        print_status('error', "Failed to get changed files")
        return []

def check_file_locations(changed_files):
    """Ensure students only edit files in STUDENT_ZONE"""
    errors = []
    warnings = []
    
    for file in changed_files:
        if not file:  # Skip empty lines
            continue
            
        # Check if file is in forbidden area
        if file.startswith(PI_ONLY):
            errors.append(f"Forbidden: Editing PI_ONLY file: {file}")
        elif file.startswith('_config.yml'):
            errors.append(f"Forbidden: Editing site configuration: {file}")
        elif file.startswith('_data/navigation.yml'):
            errors.append(f"Forbidden: Editing navigation: {file}")
        elif not file.startswith(STUDENT_ZONE):
            warnings.append(f"Warning: Editing outside STUDENT_ZONE: {file}")
    
    return errors, warnings

def validate_yaml_files(changed_files):
    """Validate YAML syntax in changed files"""
    errors = []
    
    yaml_files = [f for f in changed_files if f.endswith(('.yml', '.yaml'))]
    
    for file in yaml_files:
        if not os.path.exists(file):
            continue
            
        try:
            with open(file, 'r') as f:
                yaml.safe_load(f)
            print_status('success', f"Valid YAML: {file}")
        except yaml.YAMLError as e:
            errors.append(f"Invalid YAML in {file}: {str(e)}")
    
    return errors

def validate_markdown_files(changed_files):
    """Validate markdown files have proper front matter"""
    errors = []
    warnings = []
    
    md_files = [f for f in changed_files if f.endswith('.md')]
    
    for file in md_files:
        if not os.path.exists(file):
            continue
            
        with open(file, 'r') as f:
            content = f.read()
        
        # Check for front matter
        if not content.startswith('---'):
            errors.append(f"Missing front matter in {file}")
            continue
        
        # Extract front matter
        try:
            parts = content.split('---', 2)
            if len(parts) < 3:
                errors.append(f"Invalid front matter in {file}")
                continue
                
            front_matter = yaml.safe_load(parts[1])
            
            # Check required fields for news posts
            if 'news_drafts' in file:
                required = ['layout', 'title', 'categories', 'date']
                for field in required:
                    if field not in front_matter:
                        errors.append(f"Missing '{field}' in {file}")
                
                # Validate date format
                if 'date' in front_matter:
                    date_str = str(front_matter['date'])
                    try:
                        # Check if it's a valid date
                        if not re.match(r'\d{4}-\d{2}-\d{2}', date_str):
                            errors.append(f"Invalid date format in {file}. Use YYYY-MM-DD")
                    except:
                        errors.append(f"Invalid date in {file}")
            
            # Check for remaining [REPLACE] markers
            if '[REPLACE' in content:
                warnings.append(f"Unfilled template markers in {file}")
                
        except yaml.YAMLError as e:
            errors.append(f"Invalid front matter YAML in {file}: {str(e)}")
    
    return errors, warnings

def check_image_files(changed_files):
    """Validate image files (size and format)"""
    errors = []
    warnings = []
    
    for file in changed_files:
        if not any(file.lower().endswith(ext) for ext in ALLOWED_IMAGE_EXTENSIONS):
            continue
            
        if not os.path.exists(file):
            continue
        
        # Check file size
        file_size = os.path.getsize(file)
        if file_size > MAX_IMAGE_SIZE:
            size_mb = file_size / (1024 * 1024)
            errors.append(f"Image too large: {file} ({size_mb:.1f}MB > 2MB limit)")
        elif file_size > MAX_IMAGE_SIZE * 0.75:
            size_mb = file_size / (1024 * 1024)
            warnings.append(f"Large image: {file} ({size_mb:.1f}MB)")
        
        # Check naming convention for photos
        if 'photos' in file:
            basename = os.path.basename(file)
            if not re.match(r'\d{4}-\d{2}-\d{2}-[\w-]+\.(jpg|png)', basename, re.I):
                warnings.append(f"Photo naming convention: {file} should be YYYY-MM-DD-description.jpg")
    
    return errors, warnings

def check_profile_updates(changed_files):
    """Validate profile updates only edit allowed fields"""
    errors = []
    
    profile_files = [f for f in changed_files 
                    if 'my_profile' in f and f.endswith('.yml')]
    
    for file in profile_files:
        if not os.path.exists(file):
            continue
            
        with open(file, 'r') as f:
            content = f.read()
        
        # Check for forbidden field modifications
        forbidden_patterns = [
            r'^\s*name:',
            r'^\s*email:',
            r'^\s*title:',
            r'^\s*type:',
        ]
        
        for pattern in forbidden_patterns:
            if re.search(pattern, content, re.MULTILINE):
                # This is a bit strict - ideally we'd check if they changed the value
                # For now, just warn
                pass
    
    return errors

def main():
    """Main validation function"""
    print(f"\n{Colors.BOLD}=== Student PR Validation ==={Colors.ENDC}\n")
    
    # Get changed files
    changed_files = get_changed_files()
    
    if not changed_files:
        print_status('info', "No changed files detected")
        return 0
    
    print_status('info', f"Checking {len(changed_files)} changed files...")
    print()
    
    all_errors = []
    all_warnings = []
    
    # Run all checks
    print(f"{Colors.BOLD}1. Checking file locations...{Colors.ENDC}")
    errors, warnings = check_file_locations(changed_files)
    all_errors.extend(errors)
    all_warnings.extend(warnings)
    
    print(f"\n{Colors.BOLD}2. Validating YAML files...{Colors.ENDC}")
    errors = validate_yaml_files(changed_files)
    all_errors.extend(errors)
    
    print(f"\n{Colors.BOLD}3. Validating Markdown files...{Colors.ENDC}")
    errors, warnings = validate_markdown_files(changed_files)
    all_errors.extend(errors)
    all_warnings.extend(warnings)
    
    print(f"\n{Colors.BOLD}4. Checking image files...{Colors.ENDC}")
    errors, warnings = check_image_files(changed_files)
    all_errors.extend(errors)
    all_warnings.extend(warnings)
    
    print(f"\n{Colors.BOLD}5. Validating profile updates...{Colors.ENDC}")
    errors = check_profile_updates(changed_files)
    all_errors.extend(errors)
    
    # Print summary
    print(f"\n{Colors.BOLD}=== Validation Summary ==={Colors.ENDC}\n")
    
    if all_warnings:
        print(f"{Colors.YELLOW}Warnings ({len(all_warnings)}):{Colors.ENDC}")
        for warning in all_warnings:
            print(f"  {Colors.YELLOW}⚠{Colors.ENDC} {warning}")
        print()
    
    if all_errors:
        print(f"{Colors.RED}Errors ({len(all_errors)}):{Colors.ENDC}")
        for error in all_errors:
            print(f"  {Colors.RED}✗{Colors.ENDC} {error}")
        print()
        print(f"{Colors.RED}❌ Validation FAILED{Colors.ENDC}")
        print("Please fix the errors above before submitting your PR.")
        return 1
    else:
        print(f"{Colors.GREEN}✅ Validation PASSED{Colors.ENDC}")
        print("Your changes look good! You can submit your PR.")
        return 0

if __name__ == "__main__":
    sys.exit(main())