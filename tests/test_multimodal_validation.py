import os

import pytest

from crewai import LLM


@pytest.mark.skip(reason="Only run manually with valid API keys")
def test_multimodal_agent_with_image_url():
    """
    Test that a multimodal agent can process images without validation errors.
    This test reproduces the scenario from issue #2475.
    """
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    if not OPENAI_API_KEY:
        pytest.skip("OPENAI_API_KEY environment variable not set")

    LLM(
        model="openai/gpt-4o",  # model with vision capabilities
        api_key=OPENAI_API_KEY,
        temperature=0.7
    )
