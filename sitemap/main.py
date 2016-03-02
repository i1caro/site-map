import re
import xml.etree.ElementTree as XmlTree
from functools import partial
from urlparse import urljoin

import requests

from bs4 import BeautifulSoup


BAD_RESPONSE_VALUE = 400


def get_links(html):
  soup = BeautifulSoup(html, 'html.parser')
  return [link.get('href', '') for link in soup.find_all('a')]


def join_urls(url, links):
  return map(
    partial(urljoin, url),
    links,
  )


def filter_hash(links):
  return map(lambda x: x.split('#')[0], links)


def filter_question(links):
  return map(lambda x: x.split('?')[0], links)


def truncated_slash(links):
  match = re.compile('/$')
  return map(lambda x: match.sub('', x), links)


def exclude_files(links):
  rexp = re.compile('.*\.\w+$')
  return [link for link in links if not rexp.match(link)]


def clean_links(url, links):
  result = join_urls(url, links)
  result = filter_hash(result)
  result = filter_question(result)
  result = truncated_slash(result)
  result = exclude_files(result)
  return result


class Crawler(object):
  def __init__(self, url):
    self.base_url = url
    self.to_visit = set([url])
    self.visited = {}

  def run(self):
    for response in self.visit_sites():
      self.to_visit.update(self.new_links(response))
    return [url for url, valid in self.visited.items() if valid]

  def filter_by_url(self, links):
    return filter(lambda x: self.base_url in x, links)

  def new_links(self, response):
    raw_links = get_links(response.text)
    links = clean_links(response.url, raw_links)
    return [
      link for link in self.filter_by_url(links)
      if link not in self.visited
    ]

  def visit_sites(self):
    while(True):
      try:
        yield self.visit_one(self.to_visit.pop())
      except IndexError:
        raise StopIteration

  def visit_one(self, url):
    try:
      response = requests.get(url)
      print url
    except:
      self.visited[url] = False
    else:
      self.visited[url] = self.good_response(response)
      return response

  def good_response(self, response):
    return response.status_code < BAD_RESPONSE_VALUE

# def build_xml(links):


def build_site_map(url):
  from pprint import pprint
  pprint(Crawler(url).run())

if __name__ == '__main__':
  build_site_map(
    url='https://www.elastichosts.com'
  )
