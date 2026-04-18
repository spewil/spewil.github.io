# spewil.github.io (Pelican)

Source branch for the site built with Pelican.

## Workflow

- Write/edit content in `content/`
- Edit templates and styles in `themes/brutalist/`
- Live preview with:
  - `uv run -- make devserver`
- One-off build with:
  - `uv run -- make html`
- Publish to `gh-pages` with one command:
  - `uv run -- make publish-live`
- Publish to `gh-pages` and also update `master`:
  - `uv run -- make publish-all`

Generated output is written to `output/`.

Recommended flow:
1. `uv run -- make devserver` and test locally
2. `uv run -- make publish-live` to regenerate, update `gh-pages`, and push

If you also want `master` updated from your current branch tip:
- `uv run -- make publish-all`

## Content Layout

- Posts: `content/posts/*.md`
- Pages: `content/pages/*.md`
- Static assets: `content/images/` and `content/extra/`

## Post Semantics

### Marginalia Notes

Posts support right-side marginalia notes via raw HTML in Markdown:

```html
<aside class="marginalia">
  this is a side note.
</aside>
```

You can also use inline form:

```html
<span class="marginalia">small side note.</span>
```

Behavior:
- Desktop: note floats on the right margin
- Mobile: note becomes inline block with left border

### Quotes

Any Markdown blockquote in posts is styled as italic automatically.

Example:

```md
> This passage will render in italics on post pages.
```
