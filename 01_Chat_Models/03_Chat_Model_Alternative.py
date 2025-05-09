from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

messages = [
    SystemMessage(content="Solve the following Math problem"),
    HumanMessage(content="What is the square root of 49 ?")
]

# OpenAI Model
model = ChatOpenAI(model="gpt-4o")
result = model.invoke(messages)

# Anthropic Model
model = ChatAnthropic(model="claude-3-opus-20240229")
result = model.invoke(messages)

# Google Gemini Model
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
result = model.invoke(messages)

