"""
Detect the programming language.
"""

from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate

from pypacter import models


def language_detector(code_snippet: str) -> str:
    """
    Detects the most likely programming language for a given code snippet.

    Args:
    code_snippet (str): The input code snippet.

    Returns:
    The detected programming language.
    """
    template = "I want you to act as a programming language interpreter and"
    "tell me the name of a programming language for '{code_snippet}' code"
    "script."
    prompt = PromptTemplate(
        input_variables=["code_snippet"],
        template=template
        )
    chain = LLMChain(llm=models.DEFAULT_MODEL, prompt=prompt)
    output = chain.run({"code_snippet": code_snippet})
    return str(output["text"]).lower()
