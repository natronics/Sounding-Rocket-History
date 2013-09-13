---
layout: base
title: Sounding Rocket History
---

# Sounding Rockets

_Sounding rockets_ are relatively small rockets which carry scientific
instruments to high altitudes. They are usually unguided and fin-stabilized.
The name comes from the nautical term to “take a sounding” or measurement of
the depth of water under a ship. Sounding rockets were especially important to
scientists after World War II, when space science was in its infancy.
{: .col-lg-7}

Many thousands of sounding rockets have been launched.
{: style='clear:both;'}

---

#### Launches by Year:
<ul>
{% for post in site.categories.year %}
  <li><a href="{{ post.url | remove_first:'/'}}">{{ post.title }}</a> <span class="num">({{ post.tags }} launches)</span></li>
{% endfor %}
</ul>

---

#### Launches by Vehicle:

<ul>
{% for post in site.categories.launch-vehicle %}
  <li><a href="{{ post.url | remove_first:'/'}}">{{ post.title }}</a> <span class="num">({{ post.tags }} launches)</span></li>
{% endfor %}
</ul>

---

#### Launches by Location:

<ul>
{% for post in site.categories.location %}
  <li><a href="{{ post.url | remove_first:'/'}}">{{ post.title }}</a> <span class="num">({{ post.tags }} launches)</span></li>
{% endfor %}
</ul>
