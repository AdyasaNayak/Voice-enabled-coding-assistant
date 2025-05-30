from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()


api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("❌ GEMINI_API_KEY environment variable not set!")


llm = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-flash",  # or "models/gemini-1.5-flash"
    temperature=0.7,
    google_api_key=api_key  # pass it securely
)


prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI coding assistant."),
    ("human", "{question}")
])


chain = prompt | llm | StrOutputParser()


def get_answer(question: str) -> str:
    return chain.invoke({"question": question})
