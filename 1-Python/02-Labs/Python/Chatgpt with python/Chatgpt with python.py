import openai
import os

#openai.api_key = os.getenv("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")  # replace with your API key
openai.api_key = "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"
def ask_chatgpt(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    return response.choices[0].text.strip()
response = ask_chatgpt("Hello, can you tell me a joke?")
print(response)
