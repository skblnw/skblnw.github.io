# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview
This is a Jekyll-based GitHub Pages site using the Minimal Mistakes remote theme (v4.27.3). The site is hosted on GitHub Pages and uses the standard Jekyll static site generator.

## Development Commands

### Essential Commands
- **Start development server**: `bundle exec jekyll serve`
- **Build site**: `bundle exec jekyll build`
- **Install/update dependencies**: `bundle install`
- **Update Gemfile.lock**: `bundle update`

### Testing and Validation
- **Check Jekyll build**: `bundle exec jekyll build --verbose`
- **Serve with drafts**: `bundle exec jekyll serve --drafts`

## Architecture and Structure

### Core Configuration
- **`_config.yml`**: Main Jekyll configuration file. Contains site settings, theme configuration, and plugin definitions. Uses remote_theme for Minimal Mistakes.
- **`Gemfile`**: Ruby dependencies - uses `github-pages` gem for GitHub Pages compatibility and `jekyll-include-cache` for theme support.

### Content Structure
- **`_posts/`**: Blog posts in YYYY-MM-DD-title.markdown format
- **`index.markdown`**: Homepage with `layout: home`
- **`about.markdown`**: About page with `layout: page`
- **`404.html`**: Custom 404 error page

### Theme System
The site uses Minimal Mistakes remote theme which provides:
- Responsive layouts
- Multiple skin options
- Built-in archive pages
- Navigation support
- Social media integration

When modifying layouts or includes, refer to the [Minimal Mistakes documentation](https://mmistakes.github.io/minimal-mistakes/) as the theme files are not stored locally.

### Deployment
- **Primary branch**: `gh-pages` (deployment branch)
- **Main branch**: `main` (for pull requests)
- Site automatically deploys to GitHub Pages when changes are pushed to `gh-pages` branch

## Key Development Notes
- Jekyll version is pinned to 3.10.0 (GitHub Pages version)
- Always use `bundle exec` prefix for Jekyll commands to ensure correct gem versions
- The remote theme means theme files are not editable locally - use Jekyll's override mechanism for customizations
- Add custom CSS in `assets/css/main.scss` with proper front matter
- Custom JavaScript goes in `assets/js/` directory