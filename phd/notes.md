# Notes


## Annotator (seems to be defunct?)

add this to the page:

```javascript
<script src="http://assets.annotateit.org/annotator/v1.2.5/annotator-full.min.js"></script>
<link rel="stylesheet" href="http://assets.annotateit.org/annotator/v1.2.5/annotator.min.css">
```

add this to the content

```javascript
jQuery(function ($) {
    $('#content').annotator();
});
```

## Hypothes.is

To add Hypothesis to your web site, simply add the following line to the HTML source of your page:

```javascript
<script src="https://hypothes.is/embed.js" async></script>
```

You can configure Hypothesis by including a config tag above the the script tag. For example, the following arrangement will ensure that our yellow highlights are hidden by default:

```javascript
<script type="application/json" class="js-hypothesis-config">

{"showHighlights": false}

</script>

<script src="https://hypothes.is/embed.js" async></script>
```

configuration documentation [here](https://h.readthedocs.io/projects/client/en/latest/publishers/config/)
