from utils.langchain_agent import create_agent
from utils.io_handler import get_user_input, show_output
from utils.memory_manager import store_interaction

# Initialize the agent
agent = create_agent()

# Run the loop
if __name__ == "__main__":
    while True:
        dish = get_user_input()
        if dish.lower() in ["exit", "quit"]:
            print("Exiting the nutrition tracker.")
            break

        try:
            result = agent.run(dish)
            show_output(result)
            store_interaction(dish, result)
        except Exception as e:
            print(f"Error: {e}")
