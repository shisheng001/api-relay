# Railway 部署指南

## 当前配置状态

✅ `railway.toml` - 已就绪
✅ `Dockerfile` - 已就绪
✅ `requirements.txt` - 已就绪
✅ `main.py` - 读取环境变量 `DASHSCOPE_API_KEY`、`PROVIDER`、`PORT`

## Railway 部署步骤

### 1. 创建项目
- 登录 https://railway.app
- New Project → Deploy from GitHub → 选择 `api_relay` 仓库
  （如果没有上传到 GitHub，先 `git init` → `git add .` → `git commit`，再推送到 GitHub）

### 2. 设置环境变量（在 Railway Dashboard）
进入项目 → Variables，添加：

| 变量名 | 值 |
|--------|----|
| `DASHSCOPE_API_KEY` | `sk-5cafe647a5ac4ac991d8266c9e972f57` |
| `PROVIDER` | `bailian` |
| `PORT` | `8000` |

> ⚠️ Railway 会将环境变量加密存储，不会出现在仓库中

### 3. 部署
- Railway 自动检测到 Dockerfile 开始构建
- 构建完成后获得固定域名：`xxx.up.railway.app`

### 4. 更新推广文案
获得固定域名后，更新：
- `api_relay/PROMOTION.md` 中的 URL
- `api_relay/templates/index.html` 中的公网地址
- 小红书笔记描述中的地址

## GitHub 准备（如未上传）

```bash
cd api_relay
git init
git add .
git commit -m "api relay v1.0"
# 创建 GitHub 仓库后
git remote add origin https://github.com/<用户名>/api-relay.git
git push -u origin main
```

## Railway CLI 方式（备选）

```bash
npm install -g railway
railway login
cd api_relay
railway init
railway up
railway variables set DASHSCOPE_API_KEY=sk-xxx
railway domain
```
