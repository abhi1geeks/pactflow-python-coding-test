"""
Base routes for the API.

The routes in this module serve a very basic purpose, such as health checks and
version information.
"""

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from pypacter.programming_lang_detector import detect_language
from pypacter_api import get_version

router = APIRouter()


@router.post("/detect-programming-language", tags=["Language"])
async def detect_programming_language_api(code_snippet: str) -> JSONResponse:
    """
    Endpoint to detect the language of a code snippet.

    Accepts a POST request with a text payload containing the code snippet.

    Args:
    code_snippet: The code snippet to analyze.

    Returns:
    A JSON response containing the detected language.
    """
    language = detect_language(code_snippet)
    return JSONResponse(content={"language": language})


@router.get("/health", tags=["health"])
async def health() -> JSONResponse:
    """
    Health check.

    Returns:
        A JSON response indicating the health of the API.
    """
    return JSONResponse(content={"status": "ok"})


@router.get("/version", tags=["version"])
async def version() -> JSONResponse:
    """
    Get the version of the API.

    Returns:
        A JSON response containing the version of the API.
    """
    return JSONResponse(content={"version": get_version()})
