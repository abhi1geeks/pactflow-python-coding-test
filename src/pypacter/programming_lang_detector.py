"""
This module will be responsible for LLM logic.

i.e. detect the programming language
"""

from transformers import AutoModelForCausalLM, AutoTokenizer


def detect_language(code_snippet: str) -> str:
    """
    Detects the programming language of the code snippet.

    Args:
    code_snippet: The code snippet to analyze.

    Returns:
    The detected programming language.
    """
    try:
        # Load the LLM Model
        model_name = "bigcode/starcoder"
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name)

        # Tokenize and Generate Predictions
        inputs = tokenizer.encode(
            code_snippet, return_tensors="pt", max_length=512, truncation=True
        )
        outputs = model.generate(inputs)
        return tokenizer.decode(outputs[0], skip_special_tokens=True)
    except IndexError:
        return "Not Known"
