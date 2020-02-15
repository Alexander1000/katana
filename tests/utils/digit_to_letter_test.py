import unittest
import src.utils.digit_to_letter as digit_to_letter


class TestSanitizeMethod(unittest.TestCase):
    def testConvert_SomeDigit01_ExpectedResult(self):
        self.assertEqual('u0Cd', digit_to_letter.digit_to_letter(7866765))

    def testConvert_SomeDigit02_ExpectedResult(self):
        self.assertEqual('1uhXMZ', digit_to_letter.digit_to_letter(1581759549))

    def testConvert_SomeDigit03_ExpectedResult(self):
        self.assertEqual('zZMRCIOA', digit_to_letter.digit_to_letter(158175954914468))


if __name__ == '__main__':
    unittest.main()
