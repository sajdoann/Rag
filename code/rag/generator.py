from llm_interface import get_llm_interface

def generate_answer(query, context_docs, provider="huggingface", model_path="Qwen/DistilQwen-1.5B"):
    llm = get_llm_interface(provider=provider, model_path=model_path)
    context = "\n".join(context_docs)
    prompt = f"Answer the following question based on the context below.\n\nContext:\n{context}\n\nQuestion: {query}"
    return llm.generate_completion(prompt)