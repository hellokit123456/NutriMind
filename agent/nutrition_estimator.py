from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
from langchain.chains import LLMChain

llm = Ollama(model="mistral")  # Swapped to use Ollama's Mistral model

prompt = PromptTemplate.from_template(
    """
    Given the following list of ingredients and a brief cooking method, estimate the nutritional profile of the final dish.

    Ingredients:
    {ingredients}

    Cooking Method:
    {method}

    Return the total estimated nutrition in this format:
    Calories: X kcal
    Protein: Y g
    Fat: Z g
    Carbohydrates: W g
    """
)

chain = LLMChain(llm=llm, prompt=prompt, output_parser=StrOutputParser())

def estimate_nutrition(ingredients: list[str], method: str) -> str:
    return chain.invoke({"ingredients": ", ".join(ingredients), "method": method})
