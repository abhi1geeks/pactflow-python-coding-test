import unittest

from pypacter.programming_lang_detector import detect_language


class TestProgrammingLanguageDetection(unittest.TestCase):
    """
    Test case for the language detection function.
    """

    def test_programming_lang_detector_functionality(self) -> None:
        """
        Test the programming_lang_detector function with a simple code snippet.
        """
        # Creating a simple Python code snippet
        python_code_snippet = "print('Hello, world!')"

        # Calling the detect_language function for output
        detected_language = detect_language(python_code_snippet)

        # Printing the language detected
        assert "python" in detected_language.lower()


if __name__ == "__main__":
    unittest.main()
