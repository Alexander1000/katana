import unittest
import src.utils.sanitize as sanitize


class TestSanitizeMethod(unittest.TestCase):
    def testSanitize_LatinLetters_ExpectedResult(self):
        self.assertEqual('result', sanitize.sanitize('result'))

    def testSanitize_LatinLettersWithDigits_ExpectedResult(self):
        self.assertEqual('result10', sanitize.sanitize('result10'))


if __name__ == '__main__':
    unittest.main()
