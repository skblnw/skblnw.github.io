---
title: People
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
        <h4 style="font-size: 1.5rem;">{{ member.name }}</h4>
        <p style="font-size: 1.1rem;">{{ member.title }}</p>

        {% if member.email %}<i class="fa fa-envelope"></i> <em style="font-size: 0.95rem;">{{ member.email }}</em> <br>{% endif %}
        {% if member.twitter %}
          <i class="fab fa-twitter"></i> <a href="http://twitter.com/{{ member.twitter }}" target="_blank" rel="external nofollow noopener" style="font-size: 0.95rem;"> @{{ member.twitter }} </a> <br>
        {% endif %}
        {% if member.github %}
          <i class="fab fa-github"></i> <a href="https://github.com/{{ member.github }}" target="_blank" rel="external nofollow noopener" style="font-size: 0.95rem;">GitHub</a> <br>
        {% endif %}
        {% if member.linkedin %}
          <i class="fab fa-linkedin"></i> <a href="https://linkedin.com/in/{{ member.linkedin }}" target="_blank" rel="external nofollow noopener" style="font-size: 0.95rem;">LinkedIn</a> <br>
        {% endif %}
        {% if member.google_scholar %}
          <i class="fas fa-graduation-cap"></i> <a href="https://scholar.google.com/citations?user={{ member.google_scholar }}" target="_blank" rel="external nofollow noopener" style="font-size: 0.95rem;">Google Scholar</a> <br>
        {% endif %}
        {% if member.orcid %}
          <i class="fab fa-orcid"></i> <a href="https://orcid.org/{{ member.orcid }}" target="_blank" rel="external nofollow noopener" style="font-size: 0.95rem;">ORCID</a> <br>
        {% endif %}
        
        <p class="text-justify" style="font-size: 0.8rem; line-height: 1.5;">
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

<h2 id="alumni">Alumni</h2>

{% for alumni_data in site.data.authors %}
  {% assign alum = alumni_data[1] %}
  {% if alum.type == 'alumn' %}
<p><strong>{{ alum.name }}</strong> <br>
<i>previously:</i> {{ alum.title }} <br>
{% if alum.current_position %}<i>currently:</i> {{ alum.current_position }} <br>{% endif %}
</p>
  {% endif %}
{% endfor %}