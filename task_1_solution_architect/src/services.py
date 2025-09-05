import json
import os
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from openai import OpenAI
from .config import settings
from .prompts import ANALYZE_PROMPT, RECOMMEND_PROMPT
from .models import RecommendRequest

# --------------------------------------------------------------------------
# 1. Initialize OpenAI Client
# --------------------------------------------------------------------------
client = OpenAI(api_key=settings.TTTR_API_KEY)

# --------------------------------------------------------------------------
# 2. Simple Vector Store Initialization
#    This code runs once when the application starts.
# --------------------------------------------------------------------------
try:
    # Load a pre-trained model for creating sentence embeddings
    model = SentenceTransformer('all-MiniLM-L6-v2')
    knowledge_base_texts = []
    
    # Define the path to the knowledge base directory relative to this file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    kb_path = os.path.join(current_dir, "knowledge_base")

    # Check if the knowledge base directory exists
    if os.path.exists(kb_path):
        # Load all text files from the knowledge base directory
        for filename in os.listdir(kb_path):
            if filename.endswith(".txt"):
                with open(os.path.join(kb_path, filename), 'r', encoding='utf-8') as f:
                    knowledge_base_texts.append(f.read())

    # Create vector embeddings and a FAISS index if documents were found
    if knowledge_base_texts:
        print(f"Found {len(knowledge_base_texts)} document(s) for the knowledge base.")
        knowledge_base_embeddings = model.encode(knowledge_base_texts)
        
        # Create a FAISS index for efficient similarity search
        index = faiss.IndexFlatL2(knowledge_base_embeddings.shape[1])
        # The linter is incorrect here, so we add a 'type: ignore' comment to suppress the warning
        index.add(x=knowledge_base_embeddings) # type: ignore
    else:
        print("Knowledge base is empty or not found. Proceeding without RAG context.")
        index = None

except Exception as e:
    print(f"Error initializing vector store: {e}")
    index = None
# --------------------------------------------------------------------------
# 3. API Service Functions
# --------------------------------------------------------------------------
def get_analysis_from_llm(problem_statement: str) -> dict:
    """
    Calls the LLM to analyze the problem statement and returns a structured response.
    """
    prompt = ANALYZE_PROMPT.format(problem_statement=problem_statement)
    
    response = client.chat.completions.create(
        model=settings.TTTR_MODEL,
        messages=[{"role": "system", "content": prompt}],
        temperature=settings.TTTR_TEMPERATURE,
        response_format={"type": "json_object"},
    )
    
    llm_output = response.choices[0].message.content
    if llm_output:
        try:
            return json.loads(llm_output)
        except (json.JSONDecodeError, IndexError) as e:
            print(f"Error parsing LLM response for analysis: {e}")
    
    return {"description": "Error analyzing problem.", "clarifying_questions": []}


def get_recommendation_from_llm(analysis: RecommendRequest) -> dict:
    """
    Calls the LLM to generate a recommendation, enhanced with context from the vector store.
    """
    context = ""
    # If the vector store is initialized, search for relevant context
    if index and knowledge_base_texts:
        try:
            # Create an embedding for the user's problem description
            query_embedding: np.ndarray = model.encode([analysis.description])
            
            # Search the index for the top 1 most similar document
            # The linter is incorrect here, so we add a 'type: ignore' comment to suppress the warning
            distances, indices = index.search(x=query_embedding, k=1) # type: ignore
            
            # Add the retrieved text to the context string
            context += "\n\nUse the following context from a successful nonprofit project to inform your recommendation:\n---\n"
            for i in indices[0]:
                context += knowledge_base_texts[i]
            context += "\n---"
        except Exception as e:
            print(f"Error during vector search: {e}")

    # Format the final prompt with the retrieved context (if any)
    prompt = RECOMMEND_PROMPT.format(description=analysis.description, context=context)
    
    response = client.chat.completions.create(
        model=settings.TTTR_MODEL,
        messages=[{"role": "system", "content": prompt}],
        temperature=settings.TTTR_TEMPERATURE,
        response_format={"type": "json_object"},
    )
    
    llm_output = response.choices[0].message.content
    if llm_output:
        try:
            return json.loads(llm_output)
        except (json.JSONDecodeError, IndexError) as e:
            print(f"Error parsing LLM response for recommendation: {e}")
            
    return {
        "solution_summary": "Error generating recommendation.",
        "recommended_tech_stack": [],
        "initial_steps": [],
    }
