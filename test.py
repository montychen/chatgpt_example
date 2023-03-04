# -*- coding: utf-8 -*-
import openai
import time

openai.api_key = "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" # 请替换为您的API密钥

# def complete_davinci():
#     res = openai.Completion.create(
#         model="text-davinci-003", 
#         prompt="老虎和狮子谁厉害", 
#         temperature=0, 
#         max_tokens=1000) 
#     return res['choices'][0]['text']

# if __name__=="__main__":
#     print(complete_davinci())

model = "text-davinci-003" # GPT-3模型引擎
temperature = 0 # 生成的文本的随机性程度
max_tokens = 500 # 生成的文本的最大长度

def chat(prompt):
    res = openai.Completion.create(
      model=model,
      prompt=prompt,
      max_tokens=1024,
      temperature=temperature,
    )

    msg = res.choices[0].text.strip()
    return msg

if __name__=="__main__":
    # 循环多次进行问答交互
    while True:
        prompt = input("->您的问题(quit退出):")
        if prompt.lower() == "quit":
            break
        msg = chat(prompt)
        print("\n" + msg + "\n")
        time.sleep(1)
