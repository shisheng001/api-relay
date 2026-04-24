# API中转站推广文案

## 公网地址
https://stones-guns-waterproof-saying.trycloudflare.com

> ⚠️ 注意：cloudflared隧道URL每次重启会变，建议尽快迁移到固定域名或Railway部署

---

## 小红书笔记

### 笔记一（开发者向）
**标题：** 国内用AI接口不用VPN了

**正文：**
发现一个宝贝

用国产大模型API，完全兼容OpenAI格式
一行代码换个base_url就行

```python
client = OpenAI(
    api_key="你的key",
    base_url="https://你的地址/v1"
)
```

注册就送5元余额
qwen-turbo才3元/百万token
比直接买官方还便宜

国内直连，不用科学，延迟低
做项目、写工具、自动化脚本都用得上

#AI工具 #程序员 #Python #开发工具 #国产AI

---

### 笔记二（学生/小白向）
**标题：** 学AI编程再也不用买ChatGPT了

**正文：**
学Python的小伙伴看过来🙋

之前做AI相关项目最烦的就是
✗ OpenAI要信用卡
✗ 要VPN
✗ 还贵

现在有国产平替！
qwen-turbo跑普通对话，5块钱能用很久
注册免费送5元，够你学习用了

接入方式超简单，和ChatGPT API一模一样
换个地址就能跑

#Python学习 #AI编程 #大学生 #编程入门 #AI工具

---

## V2EX 帖子

**标题：** 分享一个国内直连的 OpenAI 兼容 API 中转，qwen-turbo 3元/M，注册送5元

**正文：**
最近在用阿里云百炼做了个 API 中转，分享一下给有需要的人。

**特点：**
- 国内直连，不需要代理
- 完全兼容 OpenAI 接口格式，只需改 base_url
- 按量付费，用多少付多少
- 注册即送 5 元余额试用

**价格：**
| 模型 | 输入 | 输出 |
|------|------|------|
| qwen-turbo | 3元/M | 6元/M |
| qwen-plus | 10元/M | 25元/M |
| qwen-max | 80元/M | 200元/M |

**接入示例：**
```python
from openai import OpenAI

client = OpenAI(
    api_key="sk-relay-你的key",
    base_url="https://你的域名/v1"
)

response = client.chat.completions.create(
    model="qwen-turbo",
    messages=[{"role": "user", "content": "你好"}]
)
```

地址：https://stones-guns-waterproof-saying.trycloudflare.com

有问题欢迎交流。

---

## 掘金/CSDN 文章标题备选

1. 《国内开发者如何低成本接入大模型API？附可用中转服务》
2. 《告别ChatGPT收费困境：3元/百万token的国产AI API接入指南》
3. 《qwen-turbo API接入教程：OpenAI兼容格式，国内直连》

---

## 微信群/知识星球文案

各位开发者好，最近搭了个AI API中转服务：
🔹 国内直连，不用VPN
🔹 兼容OpenAI格式，无缝替换
🔹 qwen-turbo 3元/百万token
🔹 新用户注册送5元试用

地址：https://stones-guns-waterproof-saying.trycloudflare.com

