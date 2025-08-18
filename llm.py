# llm_module.py
from transformers import pipeline
#Create a Pipeline for Text Generation
def generate_response(prompt, model_name="distilbert-base-uncased"):
    nlp = pipeline("text-generation", model=model_name)
    output = nlp(prompt, max_length=50)
    return output[0]['generated_text']
