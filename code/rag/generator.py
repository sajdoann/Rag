from llm_interface import get_llm_interface
from config import Config


def generate_answer(query, context_docs):
    # use config to get provider and model_path
    config = Config()

    llm = get_llm_interface(
        provider=config.get("llm", "provider"),
        model_path=config.get("llm", "model_path")
        )

    context = "\n".join(context_docs)
    prompt = f"Answer the following question based on the context below.\n\nContext:\n{context}\n\nQuestion: {query}"
    return llm.generate_completion(prompt)