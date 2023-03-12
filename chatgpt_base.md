# model

### gpt-3.5-turbo
```python
import openai
openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```
消息包括system(系统指令)、user(用户发言)、assistant(机器回复)这三部分，其中最重要的是系统指令，用于初始化ChatGPT的行为，也就是规定ChatGPT后续的行为模式。

- system系统指令: 有助于设置assistant机器回复的行为，比如指定角色。在下面的例子中，assistant被指示为“我是一个和尚...”。
- user用户发言:  通常是用户输入，描述用户要问的内容。
- assistant机器回复: 由于模型对过去的请求没有记忆。 用 assistant 存储先前的响应。当用户在提问时,引用了以前的消息时,后台可以自动帮助openai理解上下文。如果对话不适合模型的令牌限制，则需要以某种方式缩短它。