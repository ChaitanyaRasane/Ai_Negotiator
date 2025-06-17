from transformers import pipeline
generator = pipeline("text-generation", model="distilgpt2")

def generate_nlg_reply(msg):
    prompt = f"The buyer said: {msg}\\nSeller:"
    return generator(prompt, max_length=50)[0]['generated_text'].strip()
