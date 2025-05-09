from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from langchain_google_firestore import FirestoreChatMessageHistory
from google.cloud import firestore
load_dotenv()

PROJECT_ID = "langchain-b2879"
SESSION_ID = "user_session_new"
COLLECTION_NAME = "chat_history"

print("Init firebase client!")
client = firestore.Client(project=PROJECT_ID)

print("Init Firestore Chat Message History")
chat_history = FirestoreChatMessageHistory(
    session_id=SESSION_ID,
    collection=COLLECTION_NAME,
    client=client
)

print("Chat History Initalized!")
print("Current chat history :", chat_history.messages)
