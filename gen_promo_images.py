"""生成小红书推广配图"""
from PIL import Image, ImageDraw, ImageFont
import os

output_dir = r"c:\Users\chenl\WorkBuddy\20260420110834\api_relay\promo_images"
os.makedirs(output_dir, exist_ok=True)

W, H = 1080, 1080

# ===== 图1: 封面 =====
img = Image.new("RGB", (W, H), color=(10, 10, 26))
draw = ImageDraw.Draw(img)

# 渐变背景点缀
for i in range(0, H, 4):
    alpha = int(255 * (1 - i/H) * 0.15)
    draw.line([(0, i), (W, i)], fill=(108, 99, 255))

# 主标题区域背景
draw.rounded_rectangle([60, 200, W-60, 500], radius=24,
                        fill=(19, 19, 42), outline=(108, 99, 255), width=2)

# 尝试加载字体
font_paths = [
    "C:/Windows/Fonts/msyh.ttc",   # 微软雅黑
    "C:/Windows/Fonts/simhei.ttf", # 黑体
    "C:/Windows/Fonts/simsun.ttc", # 宋体
]
font_big = font_mid = font_sm = None
for fp in font_paths:
    if os.path.exists(fp):
        try:
            font_big = ImageFont.truetype(fp, 80)
            font_mid = ImageFont.truetype(fp, 42)
            font_sm  = ImageFont.truetype(fp, 32)
            break
        except:
            pass
if not font_big:
    font_big = ImageFont.load_default()
    font_mid = font_sm = font_big

# 主标题
lines1 = ["国内直连", "AI API"]
y = 230
for line in lines1:
    bb = draw.textbbox((0, 0), line, font=font_big)
    tw = bb[2] - bb[0]
    draw.text(((W - tw) // 2, y), line, fill=(200, 190, 255), font=font_big)
    y += 100

# 副标题
sub = "无需VPN · 兼容OpenAI格式"
bb = draw.textbbox((0, 0), sub, font=font_mid)
tw = bb[2] - bb[0]
draw.text(((W - tw) // 2, 450), sub, fill=(136, 136, 170), font=font_mid)

# 特性列表
features = [
    "✓  注册即送 5 元余额",
    "✓  qwen-turbo 3元/百万token",
    "✓  一行代码接入，零迁移成本",
    "✓  国内服务器，延迟极低",
]
y = 560
for feat in features:
    bb = draw.textbbox((0, 0), feat, font=font_sm)
    tw = bb[2] - bb[0]
    draw.text(((W - tw) // 2, y), feat, fill=(0, 200, 160), font=font_sm)
    y += 58

# 底部标签
tags = "#AI工具  #程序员  #Python  #国产AI  #开发工具"
bb = draw.textbbox((0, 0), tags, font=font_sm)
tw = bb[2] - bb[0]
draw.text(((W - tw) // 2, 940), tags, fill=(108, 99, 255), font=font_sm)

out_path = os.path.join(output_dir, "cover.png")
img.save(out_path)
print(f"saved: {out_path}")

# ===== 图2: 代码示例 =====
img2 = Image.new("RGB", (W, H), color=(13, 13, 31))
draw2 = ImageDraw.Draw(img2)

# 顶部标题
title = "30秒接入示例"
bb = draw2.textbbox((0, 0), title, font=font_mid)
tw = bb[2] - bb[0]
draw2.text(((W - tw) // 2, 60), title, fill=(200, 190, 255), font=font_mid)

# 代码背景框
draw2.rounded_rectangle([60, 130, W-60, 750], radius=20,
                         fill=(5, 5, 20), outline=(42, 42, 74), width=2)

font_code = None
code_font_paths = ["C:/Windows/Fonts/consola.ttf", "C:/Windows/Fonts/cour.ttf"]
for fp in code_font_paths:
    if os.path.exists(fp):
        try:
            font_code = ImageFont.truetype(fp, 28)
            break
        except:
            pass
if not font_code:
    font_code = font_sm

code_lines = [
    ("from openai import OpenAI", (197, 134, 192)),
    ("", None),
    ("client = OpenAI(", (224, 224, 224)),
    ('    api_key="sk-relay-你的key",', (195, 232, 141)),
    ('    base_url="https://你的域名/v1"', (195, 232, 141)),
    (")", (224, 224, 224)),
    ("", None),
    ("response = client.chat.completions.create(", (130, 170, 255)),
    ('    model="qwen-turbo",', (195, 232, 141)),
    ('    messages=[{"role": "user",', (224, 224, 224)),
    ('               "content": "你好"}]', (195, 232, 141)),
    (")", (224, 224, 224)),
    ("", None),
    ("print(response.choices[0].message.content)", (130, 170, 255)),
]

y = 155
for line, color in code_lines:
    if line and color:
        draw2.text((90, y), line, fill=color, font=font_code)
    y += 42

# 底部说明
notes = [
    "只需改2个参数：api_key 和 base_url",
    "原有OpenAI项目，零改动直接跑",
]
y = 790
for note in notes:
    bb = draw2.textbbox((0, 0), note, font=font_sm)
    tw = bb[2] - bb[0]
    draw2.text(((W - tw) // 2, y), note, fill=(0, 200, 160), font=font_sm)
    y += 56

tags2 = "#Python  #AI接口  #OpenAI  #开发效率"
bb = draw2.textbbox((0, 0), tags2, font=font_sm)
tw = bb[2] - bb[0]
draw2.text(((W - tw) // 2, 940), tags2, fill=(108, 99, 255), font=font_sm)

out2 = os.path.join(output_dir, "code_demo.png")
img2.save(out2)
print(f"saved: {out2}")
