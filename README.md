## pelican workflow 

```bash
$ pelican content -o output -s pelicanconf.py
$ ghp-import output -b gh-pages --nojekyll
$ git push 
```