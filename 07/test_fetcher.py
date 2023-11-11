import unittest
import subprocess
from unittest.mock import patch, MagicMock
from fetcher import open_urls_file, fetch_url, get_response


class TestFetcher(unittest.TestCase):

    def test_open_urls_file(self):
        urls = open_urls_file('urls.txt')
        self.assertEqual(type(urls), list)


    def test_what_we_obtain(self):
        dict_expected = {'https://en.wikipedia.org/wiki/Harry_S._Truman': "{'truman': 740, 'harry': 220, 'war': 177, 'retrieved': 133, '2012': 133}", 
                         'https://www.britannica.com/biography/Sofia-Coppola': "{'coppola': 30, 'sofia': 19, 'film': 14, 'britannica': 12, 'feedback': 12}", 
                         'https://en.wikipedia.org/wiki/Yuri_Dolgorukiy': "{'yuri': 46, 'kiev': 16, 'prince': 16, 'citation': 16, 'needed': 16}"
                         }
        command = "python fetcher.py -c 1 test_urls.txt"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        output, _ = process.communicate()
        output = str(output).split('\\r\\n')
        dict_obtained = {}
        for item in output:
            item = item.lstrip('b"').rstrip('"')
            if item:
                key, value = item.lstrip('b"').split(" : ")
                if key not in dict_obtained:
                    dict_obtained[key] = value
        with open("test_urls.txt") as f:
            urls_in_file = f.readlines()
        urls_in_file = [url.rstrip('\n') for url in urls_in_file]
        assert sorted(urls_in_file) == sorted(dict_obtained.keys())
        for url in dict_expected:
            assert dict_expected[url] == dict_obtained[url]


if __name__ == '__main__':
    unittest.main()
