---
title: Publications
layout: splash
permalink: /publications/
excerpt: "Selected lab publications, with links to papers and preprints."
tags: [publications, papers, preprints, manuscripts]
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /assets/images/publications-banner.jpg  # Add publications banner
intro:
    - title: Publications
---

{% include feature_row id="intro" type="center" %}

<!-- Parse CSV and display publications -->
{% assign papers = site.data.papers | reverse %}

<div class="feature__wrapper">
{% for paper in papers %}
  {% if paper.id != "id" %}  <!-- Skip header row -->
  <div class="feature__item--left">
    <article itemscope itemtype="http://schema.org/ScholarlyArticle">
      <div class="archive__item">
        {% if paper.image %}
        <div class="archive__item-teaser">
          <img src="/assets/images/papers/{{ paper.image }}" alt="{{ paper.title }}">
        </div>
        {% endif %}
        
        <div class="archive__item-body">
          <h3 class="archive__item-title">
            <span itemprop="name">{{ paper.title }}</span>
          </h3>
          
          <div class="archive__item-excerpt">
            <span itemprop="isPartOf" itemscope itemtype="http://schema.org/Periodical">
              <strong>{{ paper.journal }}</strong>
            </span>. 
            <span itemprop="datePublished">{{ paper.date }}</span>. 
            <span itemprop="author">{{ paper.authors }}</span>.
          </div>
          
          <p>
            {% if paper.link and paper.link != "" %}
              <a href="{{ paper.link }}" class="btn btn--primary" itemProp="sameAs">
                doi &nbsp; <i class="fas fa-external-link-alt"></i>
              </a>
            {% endif %}
            {% if paper.preprint_url and paper.preprint_url != "" %}
              <a href="{{ paper.preprint_url }}" class="btn btn--info" itemProp="url">
                {{ paper.preprint_label }} &nbsp; <i class="fas fa-external-link-alt"></i>
              </a>
            {% endif %}
          </p>
        </div>
      </div>
    </article>
  </div>
  {% endif %}
{% endfor %}
</div>

---

## Preprints

For our most recent work, please check our preprint servers:
- [arXiv](https://arxiv.org/search/?query=YourLab&searchtype=all)
- [bioRxiv](https://www.biorxiv.org/search/YourLab)
- [chemRxiv](https://chemrxiv.org/engage/chemrxiv/search-dashboard?text=YourLab)

## Google Scholar

For a complete list of publications, please visit our [Google Scholar profile](https://scholar.google.com/citations?user=YOURID).