from langchain_ollama import OllamaLLM
import os

def get_llm():
    model_type = os.getenv("MODEL_TYPE", "ollama")
    try:
        if model_type == "ollama":
            return OllamaLLM(model="llama3.1")  # Assumes 'ollama serve' is running
        else:
            raise ValueError(f"Invalid model type: {model_type}")
    except Exception as e:
        raise RuntimeError(f"Error initializing LLM: {str(e)}")