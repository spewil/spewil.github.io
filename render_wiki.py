#!/usr/bin/env python

import jinja2
from pathlib import Path

file_loader = jinja2.FileSystemLoader('.')
env = jinja2.Environment(loader=file_loader)


def render_frontpage():

    template = env.get_template('layout/frontpage.html')
    doc = template.render()
    with open("index.html", 'w') as outfile:
        outfile.write(doc)


def render_aboutpage():
    template = env.get_template('layout/about.html')
    doc = template.render()
    with open("about/index.html", 'w') as outfile:
        outfile.write(doc)


if __name__ == '__main__':
    render_frontpage()
    render_aboutpage()
