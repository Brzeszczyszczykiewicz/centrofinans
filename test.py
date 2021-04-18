import unittest
from send import exchange


class TestSend(unittest.TestCase):

        def test_area(self):
                self.assertEqual(exchange(1))
                self.assertEqual(exchange(-1))
                self.assertEqual(exchange('abc'))
