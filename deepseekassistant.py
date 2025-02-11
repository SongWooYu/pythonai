import ollama  # Ollama 라이브러리 불러오기

# DeepSeek-R1 14B 모델을 이용한 채팅 요청
response = ollama.chat(
    model='deepseek-r1:14b',  # 사용할 모델 지정
    messages=[
        {'role': 'user', 'content': '파이썬에서 리스트를 정렬하는 방법을 알려줘.'}
    ]
)

# 응답 출력
print(response)  # 전체 응답 출력
print(response['message']['content'])  # 메시지 내용 출력
