from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Example 1 : String as a template
template = """Write a {tone} email to {company} expressing interest in {position} position, 
mentioning {skill} as a key strength. Keep it to 4 lines max"""

prompt_template = ChatPromptTemplate.from_template(template=template)
prompt = prompt_template.invoke({
    "tone": "kind",
    "company": "Google",
    "position": "Research Engineer",
    "skill": "Machine learning"
})
result = model.invoke(prompt)
print(result.content)


# Example 2 : List as a template
messages = [
    ("system", "You are a good comedian who tells jokes about {topic}."),
    ("human", "Tell me {count} jokes")
]

joke_template = ChatPromptTemplate.from_messages(messages)
joke_prompt = joke_template.invoke({
    "topic": "doctors",
    "count": 2
})
joke = model.invoke(joke_prompt)
print(joke.content)
