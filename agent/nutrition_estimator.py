from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
from langchain.chains import LLMChain

llm = Ollama(model="mistral")  # Using Ollama's Mistral model

prompt = PromptTemplate.from_template(
    """
Given the following list of ingredients and a brief cooking method, estimate the nutritional profile of the final dish.

Ingredients:
{ingredients}

Cooking Method:
{method}

Return ONLY the final totals in this exact format, with no extra text or explanation and check the resulkts twice oer thrice no incorrect figures:

Calories: <number> kcal
Protein: <number> g
Fat: <number> g
Carbohydrates: <number> g
"""
)

chain = LLMChain(llm=llm, prompt=prompt, output_parser=StrOutputParser())

def estimate_nutrition(ingredients: list[str], method: str) -> str:
    return chain.invoke({"ingredients": ", ".join(ingredients), "method": method})
