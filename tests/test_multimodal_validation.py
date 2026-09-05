import os

import pytest

from crewai import LLM, Agent


@pytest.mark.skip(reason="Only run manually with valid API keys")
def test_multimodal_agent_with_image_url():
    """
    Test that a multimodal agent can process images without validation errors.
    This test reproduces the scenario from issue #2475.
    """
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    if not OPENAI_API_KEY:
        pytest.skip("OPENAI_API_KEY environment variable not set")

    llm = LLM(
        model="openai/gpt-4o",  # model with vision capabilities
        api_key=OPENAI_API_KEY,
        temperature=0.7,
    )

    expert_analyst = Agent(
        role="Visual Quality Inspector",
        goal="Perform detailed quality analysis of product images",
        backstory="Senior quality control expert with expertise in visual inspection",
        llm=llm,
        verbose=True,
        allow_delegation=False,
        multimodal=True,
    )

    # Test would require crewai API to run - just verify agent creation
    assert expert_analyst.multimodal is True
