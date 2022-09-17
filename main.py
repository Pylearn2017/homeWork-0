import unittest
from unittest.mock import patch
import io
import sys
from challenges import *


class TestChallenge1(unittest.TestCase):
    @patch('builtins.input', lambda *args: 'John')
    def test_1(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        challenge_1.main()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), 'Hello John\n')

    @patch('builtins.input', lambda *args: 'Bob')
    def test_2(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        challenge_1.main()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), 'Hello Bob\n')


# class TestChallenge2(unittest.TestCase):
#     @patch('builtins.input', side_effect=['John', 'Smith'])
#     def test_1(self, mock_input):
#         capturedOutput = io.StringIO()
#         sys.stdout = capturedOutput
#         challenge_2.main()
#         sys.stdout = sys.__stdout__
#         self.assertEqual(capturedOutput.getvalue(), 'Hello John Smith\n')

#     @patch('builtins.input', side_effect=['Mark', 'Millan'])
#     def test_1(self, mock_input):
#         capturedOutput = io.StringIO()
#         sys.stdout = capturedOutput
#         challenge_2.main()
#         sys.stdout = sys.__stdout__
#         self.assertEqual(capturedOutput.getvalue(), 'Hello Mark Millan\n')


# class TestChallenge3(unittest.TestCase):
#     def test_1(self):
#         capturedOutput = io.StringIO()
#         sys.stdout = capturedOutput
#         challenge_3.main()
#         sys.stdout = sys.__stdout__
#         output = 'What do you call a bear with no teeth?\n'
#         output += 'A gummy bear!\n'
#         self.assertEqual(capturedOutput.getvalue(), output)


# class TestChallenge4(unittest.TestCase):
#     @patch('builtins.input', side_effect=['2', '3'])
#     def test_1(self, mock_input):
#         capturedOutput = io.StringIO()
#         sys.stdout = capturedOutput
#         challenge_4.main()
#         sys.stdout = sys.__stdout__
#         self.assertEqual(capturedOutput.getvalue(), 'The total is 5\n')

#     @patch('builtins.input', side_effect=['-1', '0'])
#     def test_2(self, mock_input):
#         capturedOutput = io.StringIO()
#         sys.stdout = capturedOutput
#         challenge_4.main()
#         sys.stdout = sys.__stdout__
#         self.assertEqual(capturedOutput.getvalue(), 'The total is -1\n')


# class TestChallenge5(unittest.TestCase):
#     @patch('builtins.input', side_effect=['0', '0', '0'])
#     def test_1(self, mock_input):
#         capturedOutput = io.StringIO()
#         sys.stdout = capturedOutput
#         challenge_5.main()
#         sys.stdout = sys.__stdout__
#         self.assertEqual(capturedOutput.getvalue(), 'The answer is 0\n')

#     @patch('builtins.input', side_effect=['2', '2', '2'])
#     def test_2(self, mock_input):
#         capturedOutput = io.StringIO()
#         sys.stdout = capturedOutput
#         challenge_5.main()
#         sys.stdout = sys.__stdout__
#         self.assertEqual(capturedOutput.getvalue(), 'The answer is 8\n')

#     @patch('builtins.input', side_effect=['-15', '25', '39'])
#     def test_3(self, mock_input):
#         capturedOutput = io.StringIO()
#         sys.stdout = capturedOutput
#         challenge_5.main()
#         sys.stdout = sys.__stdout__
#         self.assertEqual(capturedOutput.getvalue(), 'The answer is 390\n')


# class TestChallenge6(unittest.TestCase):
#     @patch('builtins.input', side_effect=['0', '0'])
#     def test_1(self, mock_input):
#         capturedOutput = io.StringIO()
#         sys.stdout = capturedOutput
#         challenge_6.main()
#         sys.stdout = sys.__stdout__
#         self.assertEqual(capturedOutput.getvalue(),
#                          'You have 0 slices remaining\n')

#     @patch('builtins.input', side_effect=['2', '1'])
#     def test_2(self, mock_input):
#         capturedOutput = io.StringIO()
#         sys.stdout = capturedOutput
#         challenge_6.main()
#         sys.stdout = sys.__stdout__
#         self.assertEqual(capturedOutput.getvalue(),
#                          'You have 1 slices remaining\n')

#     @patch('builtins.input', side_effect=['15', '7'])
#     def test_3(self, mock_input):
#         capturedOutput = io.StringIO()
#         sys.stdout = capturedOutput
#         challenge_6.main()
#         sys.stdout = sys.__stdout__
#         self.assertEqual(capturedOutput.getvalue(),
#                          'You have 8 slices remaining\n')


# class TestChallenge7(unittest.TestCase):
#     @patch('builtins.input', side_effect=['John', '0'])
#     def test_1(self, mock_input):
#         capturedOutput = io.StringIO()
#         sys.stdout = capturedOutput
#         challenge_7.main()
#         sys.stdout = sys.__stdout__
#         self.assertEqual(capturedOutput.getvalue(),
#                          'John next birthday you will be 1\n')

#     @patch('builtins.input', side_effect=['Bob', '31'])
#     def test_2(self, mock_input):
#         capturedOutput = io.StringIO()
#         sys.stdout = capturedOutput
#         challenge_7.main()
#         sys.stdout = sys.__stdout__
#         self.assertEqual(capturedOutput.getvalue(),
#                          'Bob next birthday you will be 32\n')


# class TestChallenge8(unittest.TestCase):
#     @patch('builtins.input', side_effect=['10', '5'])
#     def test_1(self, mock_input):
#         capturedOutput = io.StringIO()
#         sys.stdout = capturedOutput
#         challenge_8.main()
#         sys.stdout = sys.__stdout__
#         self.assertEqual(capturedOutput.getvalue(),
#                          'Each person should pay 2.0\n')

#     @patch('builtins.input', side_effect=['9999', '13'])
#     def test_2(self, mock_input):
#         capturedOutput = io.StringIO()
#         sys.stdout = capturedOutput
#         challenge_8.main()
#         sys.stdout = sys.__stdout__
#         self.assertEqual(capturedOutput.getvalue(),
#                          'Each person should pay 769.1538461538462\n')


# class TestChallenge9(unittest.TestCase):
#     @patch('builtins.input', side_effect=['0'])
#     def test_1(self, mock_input):
#         capturedOutput = io.StringIO()
#         sys.stdout = capturedOutput
#         challenge_9.main()
#         sys.stdout = sys.__stdout__
#         self.assertEqual(
#             capturedOutput.getvalue(),
#             'In 0 days there are...\n0 hours\n0 minutes\n0 seconds\n')

#     @patch('builtins.input', side_effect=['123'])
#     def test_2(self, mock_input):
#         capturedOutput = io.StringIO()
#         sys.stdout = capturedOutput
#         challenge_9.main()
#         sys.stdout = sys.__stdout__
#         self.assertEqual(
#             capturedOutput.getvalue(),
#             'In 123 days there are...\n2952 hours\n177120 minutes\n10627200 seconds\n'
#         )


if __name__ == '__main__':
    unittest.main()
