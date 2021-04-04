## pelican workflow 

```bash
$ pelican content -o output -s pelicanconf.py
$ ghp-import output -b gh-pages
$ git push git@github.com:<github_username>/<github_username>.github.io.git gh-pages:master
```