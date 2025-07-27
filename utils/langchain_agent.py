from langchain.agents import initialize_agent, Tool
from langchain_community.chat_models import ChatOllama

from agent.recipe_extractor import extract_ingredients_and_method
from agent.nutrition_estimator import estimate_nutrition

llm = ChatOllama(model="mistral")

tools = [
    Tool(
        name="Ingredient & Method Extractor",
        func=lambda x: extract_ingredients_and_method(x),
        description="Extracts ingredients and cooking method from the name of a dish."
    ),
    Tool(
        name="Nutrition Estimator",
        func=lambda x: estimate_nutrition(x["ingredients"], x["method"]),
        description="Estimates nutritional profile based on ingredients and cooking method."
    )
]

def create_agent():
    return initialize_agent(
        tools,
        llm,
        agent="zero-shot-react-description",
        verbose=True
    )
