from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

messages = [
    SystemMessage("You are a finance expert!"),
    HumanMessage("What is value of 1 bitcoin in 2018"),
    AIMessage("No idea!")
]

result = model.invoke(messages)
print(result.content)
