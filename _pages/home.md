---
permalink: /
layout: splash
excerpt: "Structural bioinformatics and molecular dynamics laboratory at XJTLU."
tags: [structural bioinformatics, molecular dynamics, machine learning, computational biology]
header:
  image: /assets/images/bar-network.png  # Network visualization banner
feature_row:
  - image_path: /assets/images/lab-photo.jpg  # Add your lab group photo
    alt: "lab group photo"
    title: "Welcome to the CC Lab @ XJTLU"
    excerpt: "Our lab combines structural bioinformatics, molecular dynamics simulations, and machine learning methods to investigate protein structure-function relationships and develop computational tools for drug discovery.
    
    
    We're part of the [Center for Intelligent RNA Therapeutics](https://www.xjtlu.edu.cn/en/research/research-centres-and-institutes), and the [School of Science](https://www.xjtlu.edu.cn/en/study/schools/school-of-science) at Xi'an Jiaotong-Liverpool University.
    
    
    We're located in the Science Building at XJTLU's SIP campus, with connections to facilities in Shanghai, Hong Kong, and Columbus OH."
entries_layout: grid
---

{% include feature_row type="left" %}

{% assign elayout = page.entries_layout | default: 'grid' %}
<div class="entries-{{ elayout }}">
  {% for post in site.posts limit:4 %} 
    {% include archive-single.html type=elayout %}
  {% endfor %}
</div>