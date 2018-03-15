---
layout: page
title: books
permalink: /books/index.html
---

{% for book in site.books %}
<h2><a href="{{ book.url | prepend:site.baseurl }}">{{ book.title }}</a></h2><nobr><h1>{{ book.author }}</h1>
{% endfor %}
