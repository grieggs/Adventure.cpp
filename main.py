import openai

client = openai.OpenAI(
    base_url="http://localhost:8080/v1", # "http://<Your api-server IP>:port"
    api_key = "sk-no-key-required"
)

message = input()

chat = "You are ChatGPT, an AI assistant. Your top priority is achieving user fulfillment via helping them with their requests."

completion = client.chat.completions.create(
model="gpt-3.5-turbo",
messages=[
    {"role": "system", "content": "Summarize the following text in as few words as possible without sacrificing any of the most important information: "},
    {"role": "user", "content": message}
]
)

print(completion.choices[0].message)