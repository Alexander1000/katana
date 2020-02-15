import unittest
import src.utils.digit_to_letter as digit_to_letter


class TestSanitizeMethod(unittest.TestCase):
    def testConvert_SomeDigit_ExpectedResult(self):
        self.assertEqual('u0Cd', digit_to_letter.digit_to_letter(7866765))


if __name__ == '__main__':
    unittest.main()
