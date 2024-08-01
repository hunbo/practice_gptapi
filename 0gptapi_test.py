from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

os.environ.get("OPEN_API_KEY")


api_key = os.environ.get("OPEN_API_KEY")
client = OpenAI(
    api_key= api_key
)
#print("인증성공")

#gpt 모델에 질문을 보냄
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role":"system", "content":"너는 IT전문가야"},
             {"role":"user", "content":"전세계서 가장 많이 사용하는 프로그래밍 언어 top5를 얘기해줘"}
    ]        
)

print(response.choices[0].message.content)
#(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='전세계에서 가장 많이  사용되는 프로그래밍 언어의 순위는 시시각각 변하기 때문에 정확한 순위를 말씀드리기는 어렵지만, 현재로서는 다음과 같은 프로그래밍 언어가 많이 사용되고 있습니다.\n\n1. Python\n2. JavaScript\n3. Java\n4. C#\n5. PHP\n\n이 순위는 인기 있는 프로그래밍 언어들을 종합적으로 고려한 것이며, 상황에 따라 순위가 달라질 수 있습니다.', role='assistant', function_call=None, tool_calls=None))
#이게 choices[0]임 ㅇㅇ,,