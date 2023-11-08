import unittest
from unittest.mock import patch, MagicMock
from fetcher import open_urls_file, fetch_url, get_response


class TestFetcher(unittest.TestCase):

    def test_open_urls_file(self):
        urls = open_urls_file('test_urls.txt')
        self.assertEqual(urls, ['http://example.com', 'http://example.org'])


if __name__ == '__main__':
    unittest.main()