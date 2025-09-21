---
title: team
permalink: /people/
excerpt: "Current lab members and alumni."
tags: [members, people, team]
modified: 
comments: false
layout: single
---

{% for member_data in site.data.authors %}
  {% assign member = member_data[1] %}
  {% if member.type == 'member' %}
<!-- The paddingtop and margin-top edits allow anchors to link properly. -->
<div id="{{ member.name | replace: ' ', '-' | replace: '.', '' | replace: ',', '' }}" class="row" style="padding-top: 60px; margin-top: -60px; padding-left: 10px">
    <div class="col-sm-3">
        <figure>
            {% if member.avatar %}
            <img src="{{ member.avatar }}" class="img-fluid z-depth-1 rounded-circle" width="auto" height="auto" alt="{{ member.name }}">
            {% endif %}
        </figure>
    </div>

    <div class="col-sm-8">
        <h2 style="font-size: 1.75rem; font-weight: 400; margin-bottom: 0.5rem;">{{ member.name }}</h2>
        <p style="font-size: 1rem; color: #666; margin-bottom: 1rem;">{{ member.title }}</p>

        {% if member.email %}<i class="fa fa-envelope" style="color: #333;"></i> <em style="font-size: 0.9rem; color: #333;">{{ member.email }}</em> <br>{% endif %}
        {% if member.twitter %}
          <i class="fab fa-twitter" style="color: #1da1f2;"></i> <a href="http://twitter.com/{{ member.twitter }}" target="_blank" rel="external nofollow noopener" style="font-size: 0.9rem; color: #1da1f2; text-decoration: none;"> @{{ member.twitter }} </a> <br>
        {% endif %}
        {% if member.github %}
          <i class="fab fa-github" style="color: #333;"></i> <a href="https://github.com/{{ member.github }}" target="_blank" rel="external nofollow noopener" style="font-size: 0.9rem; color: #5cb85c; text-decoration: none;">GitHub</a> <br>
        {% endif %}
        {% if member.linkedin %}
          <i class="fab fa-linkedin" style="color: #0077b5;"></i> <a href="https://linkedin.com/in/{{ member.linkedin }}" target="_blank" rel="external nofollow noopener" style="font-size: 0.9rem; color: #5cb85c; text-decoration: none;">LinkedIn</a> <br>
        {% endif %}
        {% if member.google_scholar %}
          <i class="fas fa-graduation-cap" style="color: #4285f4;"></i> <a href="https://scholar.google.com/citations?user={{ member.google_scholar }}" target="_blank" rel="external nofollow noopener" style="font-size: 0.9rem; color: #5cb85c; text-decoration: none;">Google Scholar</a> <br>
        {% endif %}
        {% if member.orcid %}
          <i class="fab fa-orcid" style="color: #a6ce39;"></i> <a href="https://orcid.org/{{ member.orcid }}" target="_blank" rel="external nofollow noopener" style="font-size: 0.9rem; color: #5cb85c; text-decoration: none;">ORCID</a> <br>
        {% endif %}
        
        <p class="text-justify" style="font-size: 0.95rem; line-height: 1.6; color: #333; margin-top: 1rem;">
        {% if member.bio_long %}
          {{ member.bio_long }}
        {% elsif member.bio %}
          {{ member.bio }}
        {% endif %}
        </p>
    </div>
</div>
<hr>
  {% endif %}
{% endfor %}

<h2 id="alumni" style="font-size: 1.5rem; font-weight: 400; margin-top: 3rem; margin-bottom: 2rem;">alumni</h2>

{% for alumni_data in site.data.authors %}
  {% assign alum = alumni_data[1] %}
  {% if alum.type == 'alumn' %}
<p style="font-size: 0.95rem; line-height: 1.5; color: #333; margin-bottom: 1.5rem;"><strong>{{ alum.name }}</strong> <br>
<i>previously:</i> {{ alum.title }} <br>
{% if alum.current_position %}<i>currently:</i> {{ alum.current_position }} <br>{% endif %}
</p>
  {% endif %}
{% endfor %}