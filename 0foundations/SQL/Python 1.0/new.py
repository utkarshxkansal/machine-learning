from transformers import pipeline
generator = pipeline('text-generation', model='gpt2')
print(generator("Once upon a time",temperature=0.9,max_new_tokens=50))