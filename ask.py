import chromadb
from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()

# Set up Gemini
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Setting the environment
DATA_PATH = "data"
CHROMA_PATH = "chroma_db"
chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
collection = chroma_client.get_or_create_collection(name="growing_vegetables")

user_query = input("What do you want to know about growing vegetables?\n\n")

# Retrieve context from ChromaDB
results = collection.query(
    query_texts=[user_query],
    n_results=1
)

# Create a Gemini model instance
model = genai.GenerativeModel('gemini-2.5-flash')

# Construct the prompt for Gemini
system_prompt = f"""
You are a helpful assistant. You answer questions about growing vegetables in Florida. But you only answer based on the knowledge I'm providing you. You don't use your internal knowledge and you don't make things up. If you don't know the answer, just say: "I don't know."

--------------------
The data:
{results['documents']}
"""

# Generate a response using Gemini
response = model.generate_content(
    system_prompt + "\n\n" + user_query
)

print("\n\n---------------------\n\n")
print(response.text)