import unittest
import src.utils.sanitize as sanitize


class TestSanitizeMethod(unittest.TestCase):
    def testSanitize_LatinLetters_ExpectedResult(self):
        self.assertEqual('result', sanitize.sanitize('result'))

    def testSanitize_LatinCapitalizedLetters_ExpectedResult(self):
        self.assertEqual('RESULT', sanitize.sanitize('RESULT'))

    def testSanitize_LatinLettersWithDigits_ExpectedResult(self):
        self.assertEqual('result10', sanitize.sanitize('result10'))

    def testSanitize_CyrillicLetters_ExpectedResult(self):
        self.assertEqual('rezultat', sanitize.sanitize('результат'))

    def testSanitize_CapitalizedCyrillicLetters_ExpectedResult(self):
        self.assertEqual('REZULTAT', sanitize.sanitize('РЕЗУЛЬТАТ'))


if __name__ == '__main__':
    unittest.main()
