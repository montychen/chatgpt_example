2023年3月1日，openai官方发布了新的chatGPT的api接口。老接口的模型是`text-davinci-003`，新接口的模型是`gpt-3.5-turbo`。新接口的相应速度比原来快了很多，并且 **`支持上下文`**。 

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

- **system系统指令**: 有助于设置assistant机器回复的行为，比如指定后续用什么角色回复用户的提问。在下面的例子中，assistant被指示为“我是一个和尚...”。
- **user用户发言**:  通常是用户输入，描述用户要问的内容，也就是prompt。
- **assistant机器回复**: 由于模型对过去的请求没有记忆，默认是不能理解上下文的。 如果用 assistant 存储先前的响应，这样下一次用户再提问时,引用了以前的消息时,后台可以自动帮助openai理解上下文。如果对话超过令牌数量的限制，则需要以某种方式缩短它。
  - 使用 **gpt-3.5-turbo**，您必须保留要传递给模型的对话上下文，以生成相关的连贯响应。这就是它的设计方式。如果您的请求超过 **4096** 个标记，您甚至可能需要通过语义搜索或其他方式总结、修剪或提取相关部分来缩短它，但这本身就是一个完整的主题。