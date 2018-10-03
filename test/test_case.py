from test.bootcampers import Bootcamper
from test.lfa import LFAs
import unittest


class TestRating(unittest.TestCase):
    """Handles tests for the application"""

    def setUp(self):
        self.bootcampers = Bootcamper("username","password")

    def test_bootcamper_login(self):
        result = self.bootcampers.login("username", "password")
        self.assetEqual(result, True)

    def test_isinstance(self):
        self.assertIsInstance(self.lfa, LFAs)
    
