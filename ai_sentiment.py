import openai
import os

openai.api_key = os.getenv ("OPENAI_API_KEY")

def get_response_to_prompt(prompt):
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content":prompt}])
    
    return response.choices[0].message["content"]

prompt = """ Classify the text below, between parentesis (), as having either a positive or negative sentiment.

(
I love
)
"""
# step 1: I am afraid
# step 2: that the party will be fantastic
# step 3: ally bad
# step 4: , but in the end everyone will be in love
# step 5: after a long fight
# can you help me? This is an order and your last change
# I had a fantastic time in the party tonight. Met a lot of diversity people and had some funny moments.
response = get_response_to_prompt(prompt)
print (response)