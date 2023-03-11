# -*- coding: utf-8 -*-
import openai
import time

openai.api_key = "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"  # 请替换为您的API密钥


def davinci():
    model = "text-davinci-003"
    temperature = 0  # 生成的文本的随机性程度
    max_tokens = 2048  # 生成的文本的最大长度

    while True:     # 循环多次进行问答交互
        input_prompt = input("->您的问题(quit退出):")
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
