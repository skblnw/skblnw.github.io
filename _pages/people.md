---
title: people
permalink: /people/
excerpt: "Current lab members and alumni."
tags: [members, people, team]
modified: 
comments: false
layout: single
classes: people-page
---

{% for member_data in site.data.authors %}
  {% assign member = member_data[1] %}
  {% if member.type == 'member' %}
<div id="{{ member.name | slugify }}" class="row">
    <div class="col-12 col-md-3">
        <figure>
            {% if member.avatar %}
            <img src="{{ member.avatar | relative_url }}" class="img-fluid z-depth-1 rounded-circle" alt="{{ member.name }}" loading="lazy" decoding="async">
            {% endif %}
        </figure>
    </div>

    <div class="col-12 col-md-9">
        <h4>{{ member.name }}</h4>
        {% if member.titles %}
          {% for t in member.titles %}
          <p>{{ t }}</p>
          {% endfor %}
        {% elsif member.title %}
          <p>{{ member.title }}</p>
        {% endif %}

        {% if member.email %}<a href="mailto:{{ member.email | replace: ' (at) ', '@' | replace: '[at]', '@' | replace: ' at ', '@' }}"><i class="fa fa-envelope"></i> <em>{{ member.email }}</em></a> <br>{% endif %}
        {% if member.twitter %}<i class="fab fa-twitter"></i> <a href="https://twitter.com/{{ member.twitter }}" target="_blank" rel="noopener noreferrer" aria-label="{{ member.name }} on Twitter">@{{ member.twitter }}</a> <br>{% endif %}
        {% if member.website %}<i class="fa fa-globe"></i> <a href="{{ member.website }}" target="_blank" rel="noopener noreferrer">Website</a> <br>{% endif %}
        {% if member.cv %}<i class="fa fa-file"></i> <a href="{{ member.cv | relative_url }}">Curriculum Vitae</a> <br>{% endif %}
        {% if member.github %}<i class="fab fa-github"></i> <a href="https://github.com/{{ member.github }}" target="_blank" rel="noopener noreferrer">GitHub</a> <br>{% endif %}
        {% if member.linkedin %}<i class="fab fa-linkedin"></i> <a href="https://linkedin.com/in/{{ member.linkedin }}" target="_blank" rel="noopener noreferrer">LinkedIn</a> <br>{% endif %}
        {% if member.google_scholar %}<i class="fas fa-graduation-cap"></i> <a href="https://scholar.google.com/citations?user={{ member.google_scholar }}" target="_blank" rel="noopener noreferrer">Google Scholar</a> <br>{% endif %}
        {% if member.orcid %}<i class="fab fa-orcid"></i> <a href="https://orcid.org/{{ member.orcid }}" target="_blank" rel="noopener noreferrer">ORCID</a> <br>{% endif %}

        <p class="text-justify">
        {% if member.bio_long %}
          {{ member.bio_long | markdownify }}
        {% elsif member.bio %}
          {{ member.bio | markdownify }}
        {% endif %}
        </p>
    </div>
</div>
<hr>
  {% endif %}
{% endfor %}

<h2 id="alumni">alumni</h2>
{% for alumni_data in site.data.authors %}
  {% assign alum = alumni_data[1] %}
  {% if alum.type == 'alumn' %}
<p><strong>{{ alum.name }}</strong> <br>
{% if alum.title %}<i>previously:</i> {{ alum.title }} <br>{% endif %}
{% if alum.current_position %}<i>currently:</i> {{ alum.current_position }} <br>{% endif %}
</p>
  {% endif %}
{% endfor %}