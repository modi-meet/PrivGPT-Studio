import requests

def get_available_models():
    """
    Fetches list of available local models from Ollama.

    Returns:
    list: Names of available local models (with full tags).
    """
    try:
        res = requests.get("http://localhost:11434/api/tags", timeout=5)
        # Return full model names including tags (e.g., "gemma3:1b" instead of just "gemma3")
        return sorted(m['name'] for m in res.json().get("models", []))
    except:
        return []