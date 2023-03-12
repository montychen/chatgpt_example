# -*- coding: utf-8 -*-
import openai
import time

openai.api_key = "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"  # 请替换为您的API密钥


def davinci():
    """
    由于模型对过去的请求没有记忆, 所以davinci不能理解上下文（也就是之前的问答）。  gtp-3.5-turbo模型用 assistant 存储先前的响应，所以可以理解上下文
    """
    model = "text-davinci-003"
    temperature = 0  # 生成的文本的随机性程度
    max_tokens = 4048  # 生成的文本的最大长度

    while True:     # 循环多次进行问答交互
        input_prompt = input("->您的问题:")
        if not input_prompt.strip():      # 如果用户输入为空，退出程序
            break

        res = openai.Completion.create(
            model=model,
            prompt=input_prompt,
            max_tokens=max_tokens,
            temperature=temperature,
        )

        res = res.choices[0].text.strip()
        print("\n" + res + "\n")
        time.sleep(1)


if __name__ == "__main__":
    davinci()
