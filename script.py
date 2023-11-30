# https://github.com/openai/openai-python
from openai import OpenAI
# replace with your own api key
api_key = "YOUR_OWN_KEY"
client = OpenAI(api_key=api_key)

while True:
    prompt = input("Enter your prompt: ")

    completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )

    print(completion.choices[0].message.content)
