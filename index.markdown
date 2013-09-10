---
layout: base
title: Sounding Rocket History
---

# Placeholder

For now, this doesn't exist. Sorry.

Launches by Year:

---

<ul>
{% for post in site.categories.year %}
  <li><a href="{{ post.url | remove_first:'/'}}">{{ post.title }} <span class="num">({{ post.tags }} launches)</span></a></li>
{% endfor %}
</ul>

---

Launches by Vehicle:

<ul>
{% for post in site.categories.launch-vehicle %}
  <li><a href="{{ post.url | remove_first:'/'}}">{{ post.title }} <span class="num">({{ post.tags }} launches)</span></a></li>
{% endfor %}
</ul>

---

Launches by Location:

<ul>
{% for post in site.categories.location %}
  <li><a href="{{ post.url | remove_first:'/'}}">{{ post.title }} <span class="num">({{ post.tags }} launches)</span></a></li>
{% endfor %}
</ul>
