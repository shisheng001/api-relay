# API中转站 - 完整部署指南

## 🚀 快速开始

### 方式一：Docker部署（推荐）

```bash
cd api_relay

# 启动服务
docker-compose up -d

# 查看日志
docker-compose logs -f
```

### 方式二：直接运行

```bash
cd api_relay

# 安装依赖
pip install -r requirements.txt

# 运行
python main.py
```

访问 `http://localhost:8000` 确认服务启动。

---

## 🔧 初始化配置

### 1. 配置上游API Key

编辑 `main.py`，替换以下配置：

```python
UPSTREAM_CONFIG = {
    "openai": {
        "api_key": "YOUR-OPENAI-API-KEY",  # ← 替换
        # ...
    },
    "anthropic": {
        "api_key": "YOUR-ANTHROPIC-API-KEY",  # ← 替换
        # ...
    }
}
```

### 2. 创建管理员账号

首次运行后，通过API创建管理员：

```bash
curl -X POST http://localhost:8000/api/setup/admin \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "your_password"}'
```

或者直接操作数据库：

```sql
sqlite3 api_relay.db
sqlite> INSERT INTO admins (username, password_hash) VALUES ('admin', '上面密码的SHA256哈希');
```

### 3. 配置管理员密码哈希

创建 `init_admin.py` 并运行：

```python
import hashlib, sqlite3

password = "你的密码"
hashed = hashlib.sha256(password.encode()).hexdigest()

conn = sqlite3.connect("api_relay.db")
c = conn.cursor()
c.execute("INSERT INTO admins (username, password_hash) VALUES (?, ?)", 
          ("admin", hashed))
conn.commit()
conn.close()

print(f"管理员创建成功，密码哈希: {hashed}")
```

---

## 📡 API接口文档

### 用户接口

| 接口 | 方法 | 说明 |
|------|------|------|
| `POST /api/user/create` | POST | 创建用户（公开） |
| `GET /api/user/info` | GET | 获取用户信息（需API Key） |
| `GET /api/user/usage` | GET | 获取使用记录（需API Key） |

### 代理接口（OpenAI兼容）

| 接口 | 方法 | 说明 |
|------|------|------|
| `POST /v1/chat/completions` | POST | **核心代理接口** |
| `GET /v1/models` | GET | 列出可用模型 |

### 管理接口

| 接口 | 方法 | 说明 |
|------|------|------|
| `POST /api/admin/login` | POST | 管理员登录 |
| `POST /api/admin/user/create` | POST | 创建用户（需管理员） |
| `GET /api/admin/users` | GET | 用户列表（需管理员） |
| `POST /api/admin/recharge` | POST | 给用户充值（需管理员） |

---

## 💳 OpenAI API调用示例

### cURL

```bash
curl https://你的域名/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-your-api-key" \
  -d '{
    "model": "gpt-4o",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

### Python

```python
from openai import OpenAI

client = OpenAI(
    api_key="sk-your-api-key",
    base_url="https://你的域名/v1"  # ← 指向你的中转站
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)
```

### OpenAI SDK配置

```python
import openai

openai.api_key = "sk-your-api-key"
openai.base_url = "https://你的域名/v1"
# 无需其他配置，自动兼容
```

---

## 🏗️ 生产部署建议

### 1. 服务器选择

| 推荐 | 配置 | 说明 |
|------|------|------|
| 阿里云国际版 | 2核4G | 亚太节点，网络稳定 |
| AWS东京/新加坡 | t3.medium | 稳定但稍贵 |
| 搬瓦工CN2 GIA | 2核2G | 性价比高 |

### 2. Nginx配置示例

```nginx
server {
    listen 443 ssl http2;
    server_name your-domain.com;
    
    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;
    
    # 限流
    limit_req_zone $binary_remote_addr zone=api:10m rate=30r/s;
    
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        
        # 超时
        proxy_connect_timeout 60s;
        proxy_send_timeout 60s;
        proxy_read_timeout 120s;
    }
}
```

### 3. HTTPS（Let's Encrypt免费证书）

```bash
# 安装certbot
apt install certbot python3-certbot-nginx

# 申请证书
certbot --nginx -d your-domain.com
```

### 4. Systemd服务（开机自启）

创建 `/etc/systemd/system/api-relay.service`：

```ini
[Unit]
Description=API Relay Service
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/app/api_relay
ExecStart=/usr/bin/python3 /app/api_relay/main.py
Restart=always

[Install]
WantedBy=multi-user.target
```

启用服务：

```bash
sudo systemctl enable api-relay
sudo systemctl start api-relay
```

---

## 🔒 安全建议

1. **API Key存储**：生产环境使用环境变量而非代码硬编码
2. **数据库备份**：定期备份 `api_relay.db`
3. **HTTPS**：必须启用，防止Key明文传输
4. **限流**：Nginx配置请求限流，防止滥用
5. **日志**：定期检查日志，发现异常及时处理

---

## 📊 监控建议

### 基础监控

```bash
# 检查服务状态
curl http://localhost:8000/health

# 查看进程
ps aux | grep python

# 查看端口
netstat -tlnp | grep 8000
```

### 进阶监控（可选）

- Prometheus + Grafana：性能监控
- Sentry：错误追踪
- ELK Stack：日志分析

---

## ❓ 常见问题

### Q: 代理响应慢怎么办？
A: 检查海外服务器到OpenAI的网络延迟，考虑更换节点。

### Q: 余额扣费不准？
A: 检查 `calculate_cost` 函数的定价配置是否正确。

### Q: 如何对接微信/支付宝支付？
A: 需要申请商户号，可使用第三方聚合支付（易支付、 PaysApi等）。

### Q: 如何扩容？
A: 
1. 增加服务器配置
2. 使用负载均衡
3. 接入Redis缓存会话

---

## 📁 项目结构

```
api_relay/
├── main.py           # 主程序
├── requirements.txt  # Python依赖
├── Dockerfile        # Docker镜像
├── docker-compose.yml # Docker编排
├── nginx.conf        # Nginx配置参考
├── api_relay.db      # SQLite数据库（运行后生成）
└── templates/
    └── admin.html    # 管理后台页面
```

---

**有问题？** 根据错误信息检查日志，或查看上方常见问题。
