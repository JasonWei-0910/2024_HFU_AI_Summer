import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("openai_api_key")
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "刀劍神域,有紀絕劍",
        }
    ],
    model="gpt-3.5-turbo",
)

print(chat_completion.choices[0].message.content)