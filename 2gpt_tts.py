from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

os.environ.get("OPEN_API_KEY")


api_key = os.environ.get("OPEN_API_KEY")
client = OpenAI(
    api_key= api_key
)

from pathlib import Path

with client.audio.speech.with_streaming_response.create(
    model="tts-1",
    voice='echo',
    input="오늘은 내가 가장 행복한 날입니다."
) as response:
    response.stream_to_file("speech.mp3")