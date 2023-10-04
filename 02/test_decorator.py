import unittest
import logging
import time
from mean_decorator import mean


class MeanDecoratorTest(unittest.TestCase):
    logging.getLogger().setLevel(logging.INFO)

    def test_mean_decorator(self):
        @mean(3)
        def func():
            time.sleep(0.1)
        with self.assertLogs(level='INFO') as cm:
            func()
        self.assertIn("0.1", cm.output[0])
        with self.assertLogs(level='INFO') as cm:
            func()
        self.assertIn("0.1", cm.output[0])
        with self.assertLogs(level='INFO') as cm:
            func()
        self.assertIn("0.1", cm.output[0])

    def test_negative_value_for_mean(self):
        with self.assertRaises(ValueError):
            @mean(-10)
            def func():
                pass

    def test_mean_decorator_with_invalid_argument(self):
        with self.assertRaises(TypeError):
            @mean('invalid')
            def func():
                time.sleep(1)