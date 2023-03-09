import openai
import prompt_toolkit

# 设置 OpenAI API 密钥
openai.api_key = "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" # 请替换为您的API密钥

# 设置对话的参数
model_engine = "text-davinci-002"
chat_history = []

# 循环进行对话
while True:
    # 获取用户输入的对话信息
    user_input = prompt_toolkit.prompt("->问题: ")

    # 如果用户输入为空，退出程序
    if not user_input.strip():
        break

    # 将用户输入添加到聊天记录中
    chat_history.append(user_input)

    # 向 ChatGPT 发送请求，获取 AI 的回复
    response = openai.Completion.create(
        engine=model_engine,
        prompt='\n'.join(chat_history),
        max_tokens=2048,
        temperature=0,
        n = 1,
        stop=None,
    )

    # 将 AI 的回复添加到聊天记录中
    ai_response = response.choices[0].text.strip()
    chat_history.append(ai_response)

    # 输出 AI 的回复
    print("\n回答:", ai_response)
