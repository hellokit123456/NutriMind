# agent/recipe_extractor.py

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def get_recipe_and_ingredients_chain(llm):
    prompt = ChatPromptTemplate.from_template("""
    You are a professional nutritionist. Given the name of an Indian dish: {dish},
    output the recipe name, ingredients (with approximate quantities in grams or ml),
    and the typical cooking method.

    Format:
    Recipe Name: <recipe name>
    Ingredients:
    - <ingredient1>: <quantity>
    - <ingredient2>: <quantity>
    Cooking Method: <brief cooking method description># agent/recipe_extractor.py

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatOllama

def get_recipe_and_ingredients_chain(llm):
    prompt = ChatPromptTemplate.from_template("""
    You are a professional nutritionist. Given the name of an Indian dish: {dish},
    output the recipe name, ingredients (with approximate quantities in grams or ml),
    and the typical cooking method.

    Format:
    Recipe Name: <recipe name>
    Ingredients:
    - <ingredient1>: <quantity>
    - <ingredient2>: <quantity>
    Cooking Method: <brief cooking method description>
    """)
    return prompt | llm | StrOutputParser()

def extract_ingredients_and_method(dish_name: str) -> str:
    llm = ChatOllama(model="llama3")  # You can swap model if needed
    chain = get_recipe_and_ingredients_chain(llm)
    return chain.invoke({"dish": dish_name})

    """)
    return prompt | llm | StrOutputParser()
