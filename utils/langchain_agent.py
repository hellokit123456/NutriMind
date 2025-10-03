from agent.recipe_extractor import extract_ingredients_and_method
from agent.nutrition_estimator import estimate_nutrition

class NutritionAgent:
    def run(self, dish_name: str) -> str:
        recipe_text = extract_ingredients_and_method(dish_name)

        # crude parsing from plain text
        lines = recipe_text.splitlines()
        ingredients = [line.replace("-", "").strip() for line in lines if line.startswith("-")]
        method_lines = [line for line in lines if line.startswith("Cooking Method")]
        method = method_lines[0].replace("Cooking Method:", "").strip() if method_lines else ""

        nutrition_text = estimate_nutrition(ingredients, method)

        return f"{recipe_text}\n\n--- Nutrition Estimate ---\n{nutrition_text}"

def create_agent():
    return NutritionAgent()
