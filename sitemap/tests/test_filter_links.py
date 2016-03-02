from sitemap.main import (
  filter_by_url,
  filter_hash,
)


def test_filter_hash_empty():
  assert filter_hash([]) == []


def test_filter_hash():
  assert filter_hash([
    'http://www.w3schools.com#cuper',
    'http://www.schools.com',
    'http://www.schools.com/#wew',
  ]) == [
    'http://www.w3schools.com',
    'http://www.schools.com',
    'http://www.schools.com/',
  ]


def test_empy_links():
  content = []
  assert filter_by_url('http://www.w3schools.com', content) == []


def test_one_link():
  content = ['http://www.w3schools.com']
  assert filter_by_url('http://www.w3schools.com', content) == [
    'http://www.w3schools.com'
  ]


def test_links():
  content = [
    'http://www.w3schools.com',
    'http://www.w3schools.com/new',
    'http://www.w3schools.com/new/something/new',
    '#hashtag',
    '/old/',
    '/old',
    'something_older',
    'http://www.w4schools.com/ABC'
  ]
  assert filter_by_url('http://www.w3schools.com', content) == [
    'http://www.w3schools.com',
    'http://www.w3schools.com/new',
    'http://www.w3schools.com/new/something/new',
    'http://www.w3schools.com',
    'http://www.w3schools.com/old/',
    'http://www.w3schools.com/old',
    'http://www.w3schools.com/something_older',
  ]
