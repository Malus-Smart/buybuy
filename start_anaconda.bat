@echo off
chcp 65001 >nul
echo ========================================
echo   BuyBuy 购物商城 - Anaconda 启动脚本
echo ========================================
echo.

REM 检查是否在 conda 环境中
where conda >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ 错误: 未找到 conda 命令
    echo.
    echo 请使用 Anaconda Prompt 运行此脚本
    echo 或者将 Anaconda 添加到系统 PATH
    pause
    exit /b 1
)

echo [1/5] 检查 conda 环境...
conda env list | findstr "buybuy" >nul 2>nul
if %errorlevel% neq 0 (
    echo 环境不存在，正在创建 buybuy 环境...
    conda create -n buybuy python=3.10 -y
    if %errorlevel% neq 0 (
        echo ❌ 创建环境失败
        pause
        exit /b 1
    )
    echo ✅ 环境创建成功
) else (
    echo ✅ 环境已存在
)

echo.
echo [2/5] 激活环境...
call conda activate buybuy
if %errorlevel% neq 0 (
    echo ❌ 激活环境失败
    pause
    exit /b 1
)
echo ✅ 环境已激活

echo.
echo [3/5] 安装/更新依赖...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ⚠️ 警告: 部分依赖安装可能失败
)

echo.
echo [4/5] 执行数据库迁移...
python manage.py makemigrations
python manage.py migrate

echo.
echo [5/5] 启动开发服务器...
echo.
echo ========================================
echo   ✅ 服务器即将启动
echo.
echo   📱 前台网站: http://127.0.0.1:8000/
echo   🔧 管理后台: http://127.0.0.1:8000/admin/
echo.
echo   💡 提示: 首次运行需要创建管理员账号
echo        按 Ctrl+C 停止服务器后运行:
echo        python manage.py createsuperuser
echo.
echo   ⚠️  按 Ctrl+C 停止服务器
echo ========================================
echo.

python manage.py runserver

pause

