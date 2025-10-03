from langchain.memory import ConversationBufferMemory

# Using LangChain's ConversationBufferMemory (can be extended to Redis, Chroma, etc.)
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

def store_interaction(user_input, agent_output):
    memory.chat_memory.add_user_message(user_input)
    memory.chat_memory.add_ai_message(agent_output)

def get_chat_history():
    return memory.chat_memory.messages

def clear_memory():
    memory.clear()
