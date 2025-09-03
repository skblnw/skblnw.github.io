---
title: People
permalink: /people/
excerpt: "Current lab members and alumni."
tags: [members, people, team]
modified: 
comments: false
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /assets/images/people-banner.jpg  # Add team banner image

layout: archive
collection: people
entries_layout: grid    # list (default), grid
show_excerpts: true     # true (default), false
sort_by: title          # date (default) title
sort_order:             # forward (default), reverse
---

<section class="page__content cf">
<h2>Current Members</h2>
{% assign members = site.people | where: 'type', 'member' %}
<div class="entries-{{ page.entries_layout }}">
  {% include people-list.html entries=members sort_by=page.sort_by sort_order=page.sort_order type=page.entries_layout %}
</div>
</section>

<section class="page__content cf">
<h2>Alumni</h2>
{% assign alumni = site.people | where: 'type', 'alumn' %}
<div class="entries-{{ page.entries_layout }}">
  {% include people-list.html entries=alumni sort_by=page.sort_by sort_order=page.sort_order type=page.entries_layout %}
</div>
</section>