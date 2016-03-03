#!/usr/bin/env python
"""Site map.

Crawls a URL and outputs an xml site map to FILE

Usage:
  sitemap.py URL FILE
  sitemap.py (-h | --help)
  sitemap.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
"""

from docopt import docopt

from sitemap.main import build_site_map


if __name__ == '__main__':
  arguments = docopt(__doc__, version='SiteMap 0.1')
  build_site_map(arguments['URL'], arguments['FILE'])
