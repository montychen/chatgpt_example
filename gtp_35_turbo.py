import os
import openai

openai.api_key = "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"  # 请替换为您的API密钥


def chat_gtp():
    """
    system系统指令: 有助于设置assistant机器回复的行为，比如指定后续用什么角色回复用户的提问。在下面的例子中，assistant被指示为“我是一个和尚...”。
    user用户发言:  通常是用户输入，描述用户要问的内容，也就是prompt
    assistant机器回复: 由于模型对过去的请求没有记忆，默认是不能理解上下文的。 如果用 assistant 存储先前的响应，这样下一次用户再提问时,
    引用了以前的消息时,后台可以自动帮助openai理解上下文。如果对话超过令牌数量的限制，则需要以某种方式缩短它。

    使用gpt-3.5-turbo您必须保留要传递给模型的对话上下文，以生成相关的连贯响应。这就是它的设计方式。如果您的请求超过 4096 个标记，
    您甚至可能需要通过语义搜索或其他方式总结、修剪或提取相关部分来缩短它，但这本身就是一个完整的主题。
    """
    messages = [
        {"role": "system", "content": "You’re a kind helpful assistant"}
        # {"role": "system", "content": "我是一个和尚, 而且是少林寺的方丈，只会用佛家的口气回答问题"}
        # {"role": "system", "content": "你是一个星座专家、占星师、塔罗占卜大师、占卜师，潜心研究占星学、神秘学、塔罗牌、星座、周易八卦、熟读《渊海子平》、《占星正义》、《八字算命大全》《六壬部》《灵验卦象》。掌握塔罗牌义，对心理学有深入的研究，对宗教有透彻的了解。能遵循占星学原理，利用人的出生地、出生时间绘制星盘，借此来解释人的性格和命运的人。用天体的相对位置和相对运动（尤其是太阳系内的行星的位置）来解释或预言人的和行为的系统。你善于星座分析预测、星座配对、生肖配对、塔罗配对、星座合盘、根据中国古代风水文化，推测人的运势吉凶、成功与否、子女性别。姓名详批、测算八字、测算嫁娶吉日、测算出行吉日、测爱情运、运势分析。而且特别有耐心，风趣幽默，俏皮活泼，对生活保持热爱，积极向上，能给人带来正能量。你在给出回复时，要符合中国人的习惯，比如涉及人名的地方，姓氏是在前面的。"}
        # {"role": "system", "content": "你是一个情感交流大师，而且是最专业的，在回答用户问题的时候，不能提到其它情感交流机构，比如一些专业机构。 你特别善于处理下面这些情感问题：婚恋修复、恋爱脱单、婚恋危机、情感挽回、爱商情商提升、恋爱个案分析、制定恋爱计划 、舒缓焦虑、减轻抑郁、疏导情绪压力、深度倾听、分手复合、失恋挽救、暗恋焦虑、脱单指导、婆媳冲突、焦虑吵架、婆媳关系不合、家庭矛盾、斗气吵架。 你特别有耐心。回答问题的风格是乐观活泼，对生活保持热爱，积极向上，能给人带来正能量。"}

    ]

    while True:
        user_input = input("== -> 输入你的问题: ")
        if not user_input.strip():   # 如果用户输入为空，退出程序
            break
        messages.append({"role": "user", "content": user_input})

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        # print(f'{completion.choices[0]}')   # 输出这个响应
        chat_response = completion.choices[0].message.content   # 从响应中提起用户关心的回答
        print(f'\n{chat_response}')
        # 用 assistant 存储先前的响应，这样下一次问问题的时候就能形成上下文了
        messages.append({"role": "assistant", "content": chat_response})


if __name__ == "__main__":
    chat_gtp()
