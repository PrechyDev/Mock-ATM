#importing the functions to test
import unittest
from update_mock_atm import init

#start testing
class Testupdate_mock_atm(unittest.TestCase):
    def test_basic(self):
        testcase = 1
        expected = login()
        self.assertEqual(init(testcase), expected)
    def test_basic1(self):
        testcase = 2
        expected = register()
        self.assertEqual(init(testcase), expected)
    def test_invalid(self):
        testcase = " "
        expected = "You have selected an invalid option"
        self.assertEqual(init(testcase), expected)
    def test_invalid2(self):
        testcase = "."
        expected = "You have selected an invalid option"
        self.assertEqual(init(testcase), expected)
"""run this code to test if it works with the update_mock_atm.py file, place them in thesame directory"""


unittest.main()