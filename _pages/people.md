---
title: People
permalink: /people/
excerpt: "Current lab members and alumni."
tags: [members, people, team]
modified: 
comments: false
layout: single
---

## Current Members

{% assign members = site.data.authors | where: 'type', 'member' %}
{% for member_hash in members %}
  {% assign member = member_hash[1] %}
  <div class="person-card" style="display: flex; margin-bottom: 2em; border-bottom: 1px solid #eee; padding-bottom: 1em;">
    <div style="flex: 0 0 150px; margin-right: 20px;">
      {% if member.avatar %}
        <img src="{{ member.avatar }}" alt="{{ member.name }}" style="width: 150px; height: 150px; object-fit: cover; border-radius: 8px;">
      {% endif %}
    </div>
    <div style="flex: 1;">
      <h3 style="margin-top: 0;">{{ member.name }}</h3>
      <p><strong>{{ member.title }}</strong></p>
      {% if member.bio %}<p><em>{{ member.bio }}</em></p>{% endif %}
      {% if member.bio_long %}<div>{{ member.bio_long }}</div>{% endif %}
      <p>
        {% if member.email %}<a href="mailto:{{ member.email }}">Email</a> • {% endif %}
        {% if member.github %}<a href="https://github.com/{{ member.github }}">GitHub</a> • {% endif %}
        {% if member.linkedin %}<a href="https://linkedin.com/in/{{ member.linkedin }}">LinkedIn</a> • {% endif %}
        {% if member.google_scholar %}<a href="https://scholar.google.com/citations?user={{ member.google_scholar }}">Scholar</a> • {% endif %}
        {% if member.orcid %}<a href="https://orcid.org/{{ member.orcid }}">ORCID</a>{% endif %}
      </p>
    </div>
  </div>
{% endfor %}

## Alumni

{% assign alumni = site.data.authors | where: 'type', 'alumn' %}
{% for alumni_hash in alumni %}
  {% assign alum = alumni_hash[1] %}
  <div class="person-card" style="display: flex; margin-bottom: 2em; border-bottom: 1px solid #eee; padding-bottom: 1em;">
    <div style="flex: 0 0 150px; margin-right: 20px;">
      {% if alum.avatar %}
        <img src="{{ alum.avatar }}" alt="{{ alum.name }}" style="width: 150px; height: 150px; object-fit: cover; border-radius: 8px;">
      {% endif %}
    </div>
    <div style="flex: 1;">
      <h3 style="margin-top: 0;">{{ alum.name }}</h3>
      <p><strong>{{ alum.title }}</strong></p>
      {% if alum.bio %}<p><em>{{ alum.bio }}</em></p>{% endif %}
      {% if alum.bio_long %}<div>{{ alum.bio_long }}</div>{% endif %}
    </div>
  </div>
{% endfor %}