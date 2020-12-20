import unittest
from kmp import kmp


class KMPTest(unittest.TestCase):

    def testDefaultCases(self):
        self.assertEqual([(0, 1), (1, 2)], kmp('aa', 'aaa'))
        self.assertEqual([(0, 1), (1, 2)], kmp('bb', 'bbb'))
        self.assertEqual([(0, 2)], kmp('bba', 'bbaabbb'))

    def testUkrainianText(self):
        self.assertEqual([(0, 5)], kmp('Привіт', 'Привіт, привіт'))

    def testEmptyInput(self):
        self.assertEqual(-1, kmp('', 'text'))
        self.assertEqual(-1, kmp('pattern', ''))
