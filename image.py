# -*- coding: utf-8 -*-
import openai
import json
import os
from pathlib import Path
from base64 import b64decode
from io import BytesIO
from PIL import Image


openai.api_key = "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"  # 请替换为您的API密钥
# openai.api_key = os.getenv("OPENAI_API_KEY")


def image_to_url():
    """输出所生成图片的url"""
    response = openai.Image.create(
        prompt="An eco-friendly computer from the 90s in the style of vaporwave",
        n=1,
        size="512x512"
    )
    image_url = response['data'][0]['url']
    print(image_url)


def image_to_file():
    """生成的图片的自动保存在文件中"""
    response = openai.Image.create(
        prompt="An eco-friendly computer from the 90s in the style of vaporwave",
        n=1,
        size="512x512",
        response_format="b64_json",  # 图像作为 URL 或 Base64 数据返回, 默认是返回URL
    )
    image_data = b64decode(response["data"][0]["b64_json"])
    with open("res/output_myimage.png", mode="wb") as png:
        png.write(image_data)


def image_create_variation():
    """提供一个图片，生成它的变体"""

    # Read the image file from disk and resize it
    image = Image.open("res/use_2_create_variation.png")
    width, height = 512, 512
    image = image.resize((width, height))

    # Convert the image to a BytesIO object
    byte_stream = BytesIO()
    image.save(byte_stream, format='PNG')
    byte_array = byte_stream.getvalue()

    response = openai.Image.create_variation(
        image=byte_array,
        n=3,
        size="256x256",
        response_format="b64_json",
    )
    image_data = b64decode(response["data"][0]["b64_json"])
    with open("res/output_variation.png", mode="wb") as png:
        png.write(image_data)


if __name__ == "__main__":
    image_to_url()
    image_create_variation()
    image_to_file()
