#!/bin/bash
# 快速部署脚本 - 一键启动API中转站

set -e

echo "🚀 API中转站 - 快速部署"
echo "========================"

# 检查Python
if ! command -v python3 &> /dev/null; then
    echo "❌ 需要 Python 3.8+"
    exit 1
fi

# 检查pip
if ! command -v pip &> /dev/null; then
    echo "❌ 需要 pip"
    exit 1
fi

echo "📦 安装依赖..."
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

echo "🏗️ 初始化数据库..."
python3 -c "
from main import init_db
init_db()
print('✅ 数据库初始化完成')
"

echo "👤 创建管理员账号..."
python3 init_admin.py

echo ""
echo "✅ 部署完成！"
echo ""
echo "启动服务: python3 main.py"
echo "访问地址: http://localhost:8000"
echo "管理后台: http://localhost:8000/templates/admin.html"
echo ""
