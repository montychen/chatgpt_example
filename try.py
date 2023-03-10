import os
import openai

openai.api_key = "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"  # 请替换为您的API密钥
def chat_gtp():
    """
    system:
    user:
    assistant: 用 assistant 角色来存储先前的响应。当用户在提问时,引用了以前的消息时,在后台可以自动帮助openai理解上下文。
    """
    messages = [
        {"role": "system", "content": "You’re a kind helpful assistant"}
    ]

    while True:
        user_input = input("User: ")
        # 如果用户输入为空，退出程序
        if not user_input.strip():
            break
        messages.append({"role": "user", "content": user_input})

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        chat_response = completion.choices[0].message.content
        print(f'ChatGPT: {chat_response}')
        messages.append({"role": "assistant", "content": chat_response})


if __name__=="__main__":
    chat_gtp()

