import unittest
from src import helloworld


class helloworldTest(unittest.TestCase):
    def test_helloworld(self):
        a = helloworld.helloworld()
        assert a == 5


