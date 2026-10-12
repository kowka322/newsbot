import os
from openai import OpenAI
from sources import getnews
from dotenv import load_dotenv

load_dotenv()
LLM_URL = os.environ.get("LLM_URL", "http://localhost:11434/v1")
LLM_MODEL=os.environ.get("LLM_MODEL", "qwen3:8b")
client = OpenAI(
    base_url=LLM_URL,
    api_key="ollama",
    timeout=120
)

SYSTEM_PROMPT = """You are a news curator. You receive a numbered list of headlines.
Return ONLY the numbers of the headlines worth keeping, comma-separated (e.g. 1, 4, 7).
Keep genuinely notable news; drop ads, deals, clickbait, and trivial updates.
Output nothing except the numbers. If none are worth keeping, return nothing.
"""
PROMPT2 = """You are a news summarizer. Summarize the given text.
Use as much length as the content needs — sometimes one or two sentences,
sometimes a short paragraph — enough to convey the important details, no filler.
Summarize ONLY the given text. Do not add facts that are not there.
If the text is empty or has no real content, output nothing.
"""

def filter_news(items):
    
    numbered = ""
    for n, item in enumerate(items, 1):
        numbered += f"{n}. {item['title']}\n"
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": numbered}
    ]
    response = client.chat.completions.create(model="qwen3:8b", messages=messages)
    raw = response.choices[0].message.content
    selected = []
    for part in raw.replace("\n", ",").split(","):
        part = part.strip()
        if part.isdigit():
            n = int(part)
            if 1 <= n <= len(items):
                selected.append(items[n - 1])
    return selected
    

def summarize(text): 
    if not text.strip():
        return ""
    messages = [
        {"role": "system", "content": PROMPT2},
        {"role": "user", "content": text}]
    response = client.chat.completions.create(model="qwen3:8b", messages=messages)
    return response.choices[0].message.content