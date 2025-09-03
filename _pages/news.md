---
layout: archive
title: News
permalink: /news/
excerpt: "Latest news and updates from the lab."
tags: [news, updates, announcements]
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /assets/images/news-banner.jpg  # Add news banner
---

<div class="entries-list">
  {% for post in site.posts %}
    {% include archive-single.html %}
  {% endfor %}
</div>