from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from groq import Groq

# 🔑 Add your Groq API key here
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 1. Load resume
with open("resume.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 2. Split text
splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=50)
chunks = splitter.split_text(text)

# 3. Local embeddings (FREE)
embeddings = HuggingFaceEmbeddings(model_name="paraphrase-MiniLM-L3-v2")

# 4. Store in FAISS
db = FAISS.from_texts(chunks, embeddings)

# 5. Ask question
query = input("Ask something about your resume: ")

# 6. Retrieve relevant chunks
docs = db.similarity_search(query)

context = "\n".join([doc.page_content for doc in docs])

# 7. Send to Groq LLM
response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "user",
            "content": f"Answer based on this resume:\n{context}\n\nQuestion: {query}"
        }
    ]
)

# 8. Print answer
print("\nAnswer:\n", response.choices[0].message.content)