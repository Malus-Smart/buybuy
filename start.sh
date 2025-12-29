#!/bin/bash

echo "================================"
echo "  BuyBuy 购物商城启动脚本"
echo "================================"
echo ""

# 检查虚拟环境是否存在
if [ ! -d "venv" ]; then
    echo "[1/5] 创建虚拟环境..."
    python3 -m venv venv
else
    echo "[1/5] 虚拟环境已存在"
fi

echo ""
echo "[2/5] 激活虚拟环境..."
source venv/bin/activate

echo ""
echo "[3/5] 安装依赖..."
pip install -r requirements.txt

echo ""
echo "[4/5] 执行数据库迁移..."
python manage.py makemigrations
python manage.py migrate

echo ""
echo "[5/5] 启动开发服务器..."
echo ""
echo "================================"
echo "  服务器即将启动"
echo "  访问地址: http://127.0.0.1:8000"
echo "  管理后台: http://127.0.0.1:8000/admin"
echo ""
echo "  按 Ctrl+C 停止服务器"
echo "================================"
echo ""

python manage.py runserver

