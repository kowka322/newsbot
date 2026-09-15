from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

SYSTEM_PROMPT = """You are a news filter for a personal gaming/tech digest.
Select only the important headlines from the list.
Rules:
- drop clickbait, ads, deals and discounts
- keep real news: releases, announcements, industry events
- Use ONLY headlines from the list. Never invent or add news.
- if the list is empty, output nothing
Output:
a short numbered list, one headline per line.
"""


def filter_news(text):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": text}
    ]
    response = client.chat.completions.create(
        model="qwen3:8b",
        messages=messages
    )
    return response.choices[0].message.content




