## pelican workflow 

```bash
$ pelican content -o output -s pelicanconf.py
$ ghp-import output -b gh-pages --nojekyll
$ git push 
```

## useful pelican walkthrough

[link](https://stackoverflow.com/questions/55363180/how-do-i-choose-a-category-page-to-be-the-home-page-for-a-pelican-site)

## notes

`index.html` has to be there as the index of `articles` 

## plan

- front page
  - short intro
  - most recent N articles (click to see all-->paginated view)
  - favorite N article (click to see all-->paginated view)
  - most recent N book notes (click to see all-->paginated view)
- posts page (builtin pagination)
- favorites page (builtin pagination)
- drafts page (builtin pagination)
- about page
- pictures page
- phd page