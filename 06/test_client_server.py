import unittest
from unittest.mock import patch
from io import StringIO
from server import url_proc
from client import UrlStorage, send_url
import subprocess

class ServerTestCase(unittest.TestCase):

    def test_url_proc(self):
        url = "https://docs.python.org/3/library/threading.html"
        k = 5
        expected_result = "https://docs.python.org/3/library/threading.html : {'the': 468, 'is': 203, 'a': 179, 'to': 155, 'thread': 123}"
        result = url_proc(url, k)
        self.assertEqual(result.strip('"'), expected_result)


class ClientTestCase(unittest.TestCase):

    def test_read_urls_in_buffer(self):
        urls_file = "urls.txt"
        urls_storage = UrlStorage(urls_file)
        expected_urls = [
            "https://docs.python.org/3/library/threading.html",
            "https://proza.ru/editor/2021/05/31/423",
            "https://www.britannica.com/list/9-noteworthy-bog-bodies-and-what-they-tell-us",
            "https://www.coursera.org/"
        ]
        self.assertEqual(urls_storage.urls_buffer, expected_urls)

if __name__ == '__main__':
    unittest.main()