import unittest
import utils.sanitize as sanitize


class TestSanitizeMethod(unittest.TestCase):
    def testSanitize_LatinLetters_ExpectedResult(self):
        self.assertEquals('result', sanitize.sanitize('result'))


if __name__ == '__main__':
    unittest.main()
