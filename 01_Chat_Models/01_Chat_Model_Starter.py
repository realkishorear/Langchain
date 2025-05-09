from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
result = model.invoke("What is square root of 49 ?")
print(result.content)