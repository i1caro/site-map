from collections import namedtuple

import pytest

import requests

from sitemap.main import Crawler


@pytest.fixture
def bad_response(monkeypatch):
  def response(*args):
    raise requests.HTTPError
  monkeypatch.setattr('sitemap.main.requests.get', response)


Response = namedtuple('Response', ['status_code', 'text'])


@pytest.fixture
def good_response_bad_code(monkeypatch):
  def reponse(*args):
    return Response(400, 'text me latter')
  monkeypatch.setattr('sitemap.main.requests.get', reponse)


@pytest.fixture
def good_response(monkeypatch):
  def reponse(*args):
    return Response(200, 'text me latter')
  monkeypatch.setattr('sitemap.main.requests.get', reponse)


def test_error_url(bad_response):
  crawler = Crawler('http://www.w3schools.com')
  response = crawler.visit_one('http://www.w3schools.com')
  assert response is None
  assert crawler.visited['http://www.w3schools.com'] is False


def test_error_response_url(good_response_bad_code):
  crawler = Crawler('http://www.w3schools.com')
  response = crawler.visit_one('http://www.w3schools.com')
  assert response.text == 'text me latter'
  assert crawler.visited['http://www.w3schools.com'] is False


def test_good_response_url(good_response):
  crawler = Crawler('http://www.w3schools.com')
  response = crawler.visit_one('http://www.w3schools.com')
  assert response.text == 'text me latter'
  assert crawler.visited['http://www.w3schools.com'] is True
