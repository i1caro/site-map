from sitemap.main import get_links


def test_empy_links():
  content = """
    <!DOCTYPE html>
    <html>
    <body>

    <h1>My First Heading</h1>

    <p>My first paragraph.</p>

    </body>
    </html>
  """
  assert get_links(content) == []


def test_one_link():
  content = """
    <!DOCTYPE html>
    <html>
    <body>

    <a href="http://www.w3schools.com">This is a link</a>

    </body>
    </html>
  """
  assert get_links(content) == ['http://www.w3schools.com']


def test_several_links():
  content = """
    <!DOCTYPE html>
    <html>
    <body>

    <a href="http://www.w3schools.com">This is a link</a>
    <a href=  "#installing-a-parser">This is a hash tag</a>
    <a href=  "theme.css">This is a hash tag</a>

    </body>
    </html>
  """
  assert get_links(content) == [
    'http://www.w3schools.com',
    '#installing-a-parser',
    'theme.css',
  ]
