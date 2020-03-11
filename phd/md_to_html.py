#!/usr/bin/env python

import argparse
import sys
import pypandoc
import jinja2
# import markdown

TEMPLATE = """<!DOCTYPE html>
<html>
<head>
    <style>
        .wrap{
            max-width: 1200px;
            margin: 0 auto;
            padding: 1em;
        }
        .content{
            max-width: 650px;
            margin: 0 auto;
        }
        body {
            font-family: sans-serif;
        }
        code, pre {
            font-family: monospace;
        }
        h1 code,
        h2 code,
        h3 code,
        h4 code,
        h5 code,
        h6 code {
            font-size: inherit;
        }
    </style>
    <script src="https://hypothes.is/embed.js" async></script>
</head>
<body>
<div class="wrap">
<div class="content">
{{content}}
</div>
</div>
</body>
</html>
"""


def parse_args(args=None):
    d = 'Make a complete, styled HTML document from a Markdown file.'
    parser = argparse.ArgumentParser(description=d)
    parser.add_argument('mdfile',
                        type=argparse.FileType('r'),
                        nargs='?',
                        default=sys.stdin,
                        help='File to convert. Defaults to stdin.')
    parser.add_argument('-o',
                        '--out',
                        type=argparse.FileType('w'),
                        default=sys.stdout,
                        help='Output file name. Defaults to stdout.')
    return parser.parse_args(args)


def main(args=None):
    args = parse_args(args)
    # md = args.mdfile.read()
    # extensions = ['extra', 'smarty']
    # html = markdown.markdown(md, extensions=extensions, output_format='html5')
    # make bib file an optional argument!
    pdoc_args = ['--bibliography=bibliography.bib']
    filters = ['pandoc-citeproc']
    html = pypandoc.convert_file(args.mdfile.name,
                                 'html',
                                 format='md',
                                 extra_args=pdoc_args,
                                 filters=filters)
    doc = jinja2.Template(TEMPLATE).render(content=html)
    args.out.write(doc)


if __name__ == '__main__':
    sys.exit(main())

############

# # -*- coding: utf-8 -*-
# """procmd.procmd

# The objective of this module is to facilitate parsing documents writing in
# markdown to jinja templates through the module markdown with the possibility
# of extracting some meta information existing in the header of the markdown file.

# It is also possible to use markdown as a template using jinja. This can be done
# previously to convert markdown to html or other final formats. A bit as
# pandoc with personalized templates. You can use variables declared in the meta
# header of the markdown file as variables in the jinja template. The trick is to
# process the markdown file one for the meta, then for jinja and after for the
# final format.

# This module conjoin functionalities from markdown_ and jinja_ worlds, acting
# as a light and very specific facade of both python modules.

# :mod:`procmd` has two principal functions with diferents goals:

# * Markdown with header data and jinja code + YAML data --> Markdown text.

# * Markdown text with header data + YAML data + HTML jinja template -->
#   HTML text.

# .. author: Vicente Ramirez Perea
# .. license: MIT
# .. note::
#     With ideas from `<https://gist.github.com/glombard/7554134>`_ and
#     `<https://gist.github.com/jiffyclub/5015986>`_ . They probably were inspired
#     by `<http://flask.pocoo.org/snippets/19/>`_.

# .. warning::
#     Don't put this module in a production web site or any other type of
#     application without taking care on how to handle escaping in templates with
#     jinja. The module is intended for use in a controlled environment where you
#     know what the content of the variables could be.

# .. .. todo:: Get list of yaml files from md header

# """
# import os
# import jinja2
# import markdown
# import sys
# import yaml

# with open(os.path.join(os.path.dirname(__file__), 'VERSION')) as \
#         version_file:
#     read_version = version_file.read().strip().split('.')
# version = '{0:}.{1:}'.format(*read_version[0:2])

# def get_md_content_as_html_and_meta(md_text, extensions=None):
#     """
#     Process a markdown file to html getting the meta section

#     :param str md_text: name of markdown file.
#     :param list(str) extensions: other extensions for passing to markdown
#         module.
#     :return: dictionary with two keys.
#         *contentHtml*: with markdown transformed.
#         *meta*: with a dictionary of variables of the meta section.
#     :rtype: dict

#     .. note::
#         See in the code that :func:`markdown.Markdown` is capitalized.

#     """

#     if extensions is None:
#         extensions = []
#     extensions.extend(['meta'])
#     md = markdown.Markdown(extensions=extensions, output_format='html5')

#     return {'content': md.convert(md_text), 'meta': md.Meta}

# def clean_meta(meta):
#     """ Clean list values which have only one member.

#     Clean *meta* data coming from a markdown file processed with
#     `markdown.markdown() <http://pythonhosted.org/Markdown/reference.html>`_
#     function and extension meta enable.

#     :param dict meta: dictionary as obtained by meta extension when using
#         `markdown.markdown() <http://pythonhosted.org/Markdown/reference.html>`_
#         with keys and values as lists.

#     :return: dictionary with the same keys as meta param but the values with
#         length=1 converted to no list.
#     :rtype: dict

#     Example:

#     >>> meta = {'title': ['The Title'],'authors': ['Author One', 'Author Two']}
#     >>> clean_meta(meta) == {'title': 'The Title', 'authors': ['Author One', 'Author Two']}
#     True

#     .. note::
#         See in the code example that *title* value lost the brackets.

#     .. note::
#         The function do not cleans empty strings because it could be the
#         intended use.

#     That means you need to put list values in the markdown header as this:

#     .. code::

#         title: The Title
#         authors: Author One
#             Author Two

#     See the first author is in the same line of the variable name.

#     """
#     newmeta = {}
#     for k, v in meta.items():
#         # El modulo extension extra meta devuelve listas solo del primer
#         # No sería necesario el elemento recursivo, pero puede ser interesante
#         # para una futura particularización del tratamiento de meta
#         if isinstance(v, dict):
#             newmeta.update(clean_meta(v))
#         else:
#             if len(v) > 1:
#                 newmeta.update({k: v})
#             else:
#                 newmeta.update({k: v[0]})
#     return newmeta

# def set_yaml_data(yaml_file):
#     """Load data from YAML file

#     :param str yaml_file: Name of the YAML file.
#     :return: Dictionary populated with data in the YAML file.
#     :rtype: dict
#     """

#     if yaml_file is None:
#         ym_data = {}
#     else:
#         with (open(yaml_file, 'r')) as ymf:
#             ym_data = yaml.load(ymf)
#     return ym_data

# def process_jinja(template_dir, template_file, data):
#     """
#     Process a Jinja template with the passed data.

#     The template file could use any variable passed in the data dictionary.

#     .. note::
#         It is assumed that the jinja environment is at the same level of the
#         directory of the template file.

#     :param str template_dir: Directory name of the base for jinja environment.
#     :param str template_file: File name of the template.
#     :param dict data: Contents to pass to the template.

#     .. :param str syntax: Type of syntax of the template. Default jinja. It
#         could be also *latex*. TODO, take from cv-templating.

#     :return: Template processed.
#     :rtype: str

#     """
#     # todo link to other syntax functions

#     env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
#                              lstrip_blocks=False,
#                              trim_blocks=False)

#     template = env.get_template(template_file)

#     return template.render(data)

# def process_md_as_content_for_jinja(md_file,
#                                     template_file,
#                                     yaml_file=None,
#                                     template_dir=None,
#                                     md_extensions=None):
#     """
#     Process md as content for a jinja template

#     Function takes a markdown file, extracts meta data from header of
#     markdown file and process the content as HTML5.

#     The content and the header data are passed to a jinja template for
#     further process. In the jinja template content must be referenced as
#     md.content and data in the header as md.<variable>, with <variable> (
#     without < and >) one of the declared variables (e.g. title, authors, etc.).

#     :param str md_file: name of the markdown file. As content provider.
#     :param str template_file: name of the template file. With jinja variables
#         and blocks.
#     :param str yaml_file: If passed, data in yaml format to be used by jinja. In
#         the template, this data will have *ym* prefix (e.g. ym.publdate).
#     :param str template_dir: Directory for base template for jinja. If it is
#         not provided, the function takes directory of *md_file* as default. If
#         *template_dir* is provided, then the path of *md_file* is
#         relative to *template_dir*.
#     :param list(str) md_extensions: Extensions for passing to Markdown instance.
#     :return: An HTML str result of processing the jinja template
#     :rtype: str

#     .. seealso:: :doc:`tutorial` with an example of use.

#     .. note::
#         This function in intended to be used with output result as HTML

#     """

#     if md_extensions is None:
#         md_extensions = []
#     with open(md_file, 'r') as mdf:
#         md_str = mdf.read()

#     md_content_and_meta = get_md_content_as_html_and_meta(
#         md_str, extensions=md_extensions)
#     ym_data = set_yaml_data(yaml_file)

#     data_for_jinja = {'ym': ym_data, 'md': clean_meta(md_content_and_meta)}

#     if template_dir is None:
#         template_dir = os.path.dirname(os.path.abspath(md_file))
#         template_file = os.path.basename(template_file)

#     return process_jinja(template_dir, template_file, data_for_jinja)

# def process_md_as_jinja(md_file,
#                         yaml_file=None,
#                         template_dir=None,
#                         md_extensions=None):
#     """
#     Process markdown file as template jinja using section meta and a posible
#     YAML data file.

#     :param str md_file: markdown file as jinja template.
#     :param str yaml_file: If passed, data in yaml format to be used by jinja. In
#         the template, this data will have *ym* prefix (e.g. ym.publdate).
#     :param str template_dir: Directory for base template for jinja. If it is
#         not provided, the function takes directory of *md_file* as default. If
#         *template_dir* is provided, then the path of *md_file* is
#         relative to *template_dir*.
#     :param list(str) md_extensions: Extensions for passing to Markdown instance.
#     :returns: text processed.
#     :rtype: str

#     .. seealso:: :doc:`tutorial` with an example of use.

#     .. note::
#         This function in intended to be used with output result as markdown

#     """
#     if md_extensions is None:
#         md_extensions = []
#     with open(md_file, 'r') as mdf:
#         md_str = mdf.read()
#     md = get_md_content_as_html_and_meta(md_str, md_extensions)
#     meta = md['meta']
#     ym_data = set_yaml_data(yaml_file)
#     data = {'ym': ym_data, 'md': clean_meta(meta)}
#     template_file = md_file
#     if template_dir is None:
#         template_dir = os.path.dirname(os.path.abspath(md_file))
#         template_file = os.path.basename(md_file)
#     return process_jinja(template_dir, template_file, data)

# def create_cml_parser():
#     """Create command line parser

#     From the CLI can be accessed :func:`process_md_as_jinja` and
#     :func:`process_md_as_content_for_jinja`.

#     :return: Populated Namespace with parsed command line argument values.
#     :rtype: argparse.Namespace
#     """
#     import argparse

#     cml = argparse.ArgumentParser(description="""
#             | The intention of this module is to provide a method to
#             | pass meta information in markdown header files for
#             | using it in jinja templates.
#             |
#             | Also, to provide a method to use markdown files as jinja
#             | templates. Maybe you prefer to see the code than
#             | to install it.
#             |
#             | Warning! You are responsible of the contents of your files
#             | passed as arguments.
#             | Please, be cautious because there are no escaping in the process.
#             | You must provide it in your templates.
#             | """.replace('            | ', ''))
#     cml.add_argument("-m",
#                      "--mdfile",
#                      help="""
#             | Input markdown file. Depending of the command line argument
#             | conversiontype, it will be processed as content provider to
#             | a template file if optional argument --template is passed.
#             | If --template is not passed, then will be processed as a
#             | template itself with data in its header section (and if
#             | provided --yaml file, also with its data).
#             | """.replace('            | ', ''))
#     cml.add_argument(
#         "-c",
#         "--conversiontype",
#         choices=['astemplate', 'ascontents'],
#         help="See mdfile argument. Default astemplate if it is not provided.",
#         default='astemplate')
#     cml.add_argument(
#         "--to",
#         help="Destination file. If it is not provided output will be print "
#         "in screen.")
#     cml.add_argument("-t",
#                      "--template",
#                      help="""
#             | Template file to be used with conversiontype=ascontents.
#             | Destination will be overwrite.
#             | """.replace('            | ', ''))
#     cml.add_argument("--templatedir",
#                      help="""
#                 | Base template directory to be used if --template is provided.
#                 | If it is not provided, procmd implicitely assume that is
#                 | the same directory as the template file.
#                 | """.replace('            | ', ''))
#     cml.add_argument("-d",
#                      "--datafile",
#                      help="""
#             | Additional data file in YAML format.
#             | """.replace('            | ', ''))
#     cml.add_argument("--extensions",
#                      help="""
#             | Additional extensions to be used by markdown module (e. g.
#             | *--extensions codehilite fenced_blocks*).
#             | """.replace('            | ', ''),
#                      nargs='?')
#     cml.add_argument("-v",
#                      "--version",
#                      action='version',
#                      version='%(prog)s ' + version,
#                      help="Show program's version number and exit")
#     cml.add_argument(
#         "--test",
#         default=False,
#         action='store_true',
#         help="Execute *doctest* previously to run the chosen option.")
#     return cml

# def main():
#     """
#     The function parses the command line arguments and establish logic of CLI.

#     :return: 0 if program finish correctly.

#     """
#     cml_parser = create_cml_parser()
#     cml_args = cml_parser.parse_args()

#     # See http://stackoverflow.com/a/20350111

#     if not cml_args.test and cml_args.mdfile is None:
#         cml_parser.error('Please provide a markdown file')
#         return sys.exit(0)

#     if cml_args.test:
#         import doctest
#         doctest.testmod(verbose=True)

#     if cml_args.conversiontype == 'astemplate':
#         result = process_md_as_jinja(cml_args.mdfile, cml_args.datafile,
#                                      cml_args.templatedir, cml_args.extensions)
#     else:
#         result = process_md_as_content_for_jinja(cml_args.mdfile,
#                                                  cml_args.template,
#                                                  cml_args.datafile,
#                                                  cml_args.templatedir,
#                                                  cml_args.extensions)

#     if cml_args.to is None:
#         print(result)
#     else:
#         with open(cml_args.to, 'w') as of:
#             of.write(result)

# if __name__ == "__main__":

#     sys.exit(main())
