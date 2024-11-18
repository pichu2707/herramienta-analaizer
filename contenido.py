import requests
from requests.auth import HTTPBasicAuth
import json
import base64

from config import TOKEN_OPENAI

import openai
from openai import OpenAI

client=openai.OpenAI(api_key=TOKEN_OPENAI)

stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Say this is a test"}],
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")