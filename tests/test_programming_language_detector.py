"""
Test the programming language detector.
"""


from src.pypacter import programming_language_detector as pld


def test_python_detect_language() -> None:
    # Test with a file path
    code_snippet = """
            def add(a, b):

            #Sum two numbers

            return a + b """
    result = pld.language_detector(code_snippet=code_snippet)
    assert len(result) > 0
    assert "python" in result


def test_java_detect_language() -> None:
    # Test with a file path
    code_snippet = """
            class Test
                {
                    public static void main(String []args)
                    {
                        System.out.println("My First Java Program.");
                    }
                };
             """
    result = pld.language_detector(code_snippet=code_snippet)
    assert len(result) > 0
    assert "java" in result


def test_javascript_detect_language() -> None:
    # Test with a file path
    code_snippet = """
            console.log("Hello, World!");
             """
    result = pld.language_detector(code_snippet=code_snippet)
    assert len(result) > 0
    assert "javascript" in result


def test_c_detect_language() -> None:
    # Test with a file path
    code_snippet = """
            #include <stdio.h>
            int main() {
            // printf() displays the string inside quotation
            printf("Hello, World!");
            return 0;
            }
             """
    result = pld.language_detector(code_snippet=code_snippet)
    assert len(result) > 0
    assert "c" in result
