from ollama import chat

with open("filesm.txt","r") as file:
    file = file.read()

my_sms = f"{file}"

response = chat(
    model="gemma3:1b",
    messages=[
        {
            "role": "user",
            "content": my_sms
        }
    ]
)

print(response["message"]["content"])