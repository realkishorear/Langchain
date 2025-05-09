from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.schema import AIMessage, HumanMessage, SystemMessage

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

chat_history = []
system_response = SystemMessage("You are an helpful AI Assistant")
chat_history.append(system_response)

while True:
    query = input("Enter your prompt :")
    if query.lower() == "exit":
        break
    
    user_prompt = HumanMessage(content=query)
    chat_history.append(user_prompt)
    
    AI_Response = model.invoke(chat_history)
    chat_history.append(AI_Response.content)
    
    print(f"AI : {AI_Response.content}")

print(f"Here you go with ChatHistory : {chat_history}")