@echo off
chcp 65001 >nul
echo.
echo ========================================
echo    API中转站 - Windows 快速部署
echo ========================================
echo.

REM 检查Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [错误] 未检测到 Python，请先安装 Python 3.8+
    echo 下载地址: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [1/4] 安装依赖...
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

echo.
echo [2/4] 初始化数据库...
python -c "from main import init_db; init_db(); print('[OK] 数据库就绪')"

echo.
echo [3/4] 启动服务...
echo.
echo ========================================
echo 服务已启动！
echo 访问 http://localhost:8000 查看状态
echo 
echo 重要配置:
echo   - 编辑 main.py 设置你的 API Key
echo   - 运行 python init_admin.py 创建管理员
echo ========================================
echo.
start http://localhost:8000

python main.py
