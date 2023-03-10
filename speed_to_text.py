# coding=utf-8
import os
import openai

openai.api_key = "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" # 请替换为您的API密钥
# openai.api_key = os.getenv("OPENAI_API_KEY")

def speed_to_text():
    audio_file1 = open("res/zhi.m4a", "rb")
    audio_file2 = open("res/yue.m4a", "rb")
    audio_file3 = open("res/yue.m4a", "rb")

    transcript1 = openai.Audio.transcribe('whisper-1', audio_file1) # 把音频转换成音频所使用的语言对应的文字。
    transcript2 = openai.Audio.transcribe('whisper-1', audio_file2) 
    translate_en = openai.Audio.translate("whisper-1", audio_file3) # 把音频转换成英文文字

    print(transcript1['text']+"\n")
    print(transcript2['text']+"\n")
    print(translate_en['text'])

if __name__=="__main__":
    speed_to_text()
