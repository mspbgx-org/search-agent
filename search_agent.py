import logging
from ddgs import DDGS
from ddgs.exceptions import DDGSException, RatelimitException
from strands import Agent, tool
from strands.models import BedrockModel

logging.getLogger("strands").setLevel(logging.INFO)


@tool
def websearch(
    keywords: str, region: str = "us-en", max_results: int | None = None
) -> str:
    """Search the web to get updated information.
    Args:
        keywords (str): The search query keywords.
        region (str): The search region: wt-wt, us-en, uk-en, ru-ru, etc..
        max_results (int | None): The maximum number of results to return.
    Returns:
        List of dictionaries with search results.
    """
    try:
        results = DDGS().text(keywords, region=region, max_results=max_results)
        return results if results else "No results found."
    except RatelimitException:
        return "RatelimitException: Please try again after a short delay."
    except DDGSException as d:
        return f"DuckDuckGoSearchException: {d}"
    except Exception as e:
        return f"Exception: {e}"


bedrock_model = BedrockModel(
    model_id="eu.anthropic.claude-sonnet-4-20250514-v1:0"
)

search_agent = Agent(
    system_prompt="""You are a helpful assistant.
    Help users to find information based on their queries and answer questions.
    Use the websearch tool to find information.""",
    tools=[websearch],
    model=bedrock_model,
)


if __name__ == "__main__":
    print("\nAsk me anything! Type 'exit' to quit.\n")

    while True:
        user_input = input("\nYou > ")
        if user_input.lower() == "exit":
            print("Happy hacking!")
            break
        response = search_agent(user_input)
        print(f"\nsearch_bot > {response}")
