# 🐍 Anaconda 环境配置指南

## 使用 Anaconda 运行 BuyBuy 项目

### 系统要求

- ✅ Anaconda 或 Miniconda
- ✅ Python 3.8 或更高版本

---

## 📦 方法一：快速配置（推荐）

### 1. 创建 Conda 环境

打开 Anaconda Prompt（或终端），在项目目录下运行：

```bash
# 进入项目目录
cd E:\buybuy

# 创建新的 conda 环境（Python 3.10）
conda create -n buybuy python=3.10 -y

# 激活环境
conda activate buybuy
```

### 2. 安装依赖包

```bash
# 使用 pip 安装项目依赖
pip install -r requirements.txt
```

**或者分别安装**：
```bash
pip install Django==4.2.7
pip install Pillow==10.1.0
pip install django-crispy-forms==2.1
pip install crispy-bootstrap5==1.0.0
pip install python-decouple==3.8
```

### 3. 初始化数据库

```bash
# 创建数据库迁移文件
python manage.py makemigrations

# 执行数据库迁移
python manage.py migrate
```

### 4. 创建超级管理员

```bash
python manage.py createsuperuser
```

按提示输入：
- 用户名（例如：admin）
- 邮箱（可以跳过，直接回车）
- 密码（输入两次，密码不会显示）

### 5. 添加示例数据（可选但推荐）

```bash
python manage.py shell
```

然后在 shell 中运行：
```python
exec(open('create_sample_data.py').read())
```

输入 `exit()` 或按 `Ctrl+Z` 然后回车退出 shell。

### 6. 启动服务器

```bash
python manage.py runserver
```

看到如下信息表示成功：
```
Starting development server at http://127.0.0.1:8000/
```

### 7. 访问网站

打开浏览器访问：
- **前台**: http://127.0.0.1:8000/
- **后台**: http://127.0.0.1:8000/admin/

---

## 📋 方法二：使用 environment.yml（推荐团队协作）

我已经为您创建了一个 `environment.yml` 文件，可以一键创建环境：

```bash
# 使用 environment.yml 创建环境
conda env create -f environment.yml

# 激活环境
conda activate buybuy

# 初始化数据库
python manage.py makemigrations
python manage.py migrate

# 创建管理员
python manage.py createsuperuser

# 启动服务器
python manage.py runserver
```

---

## 🔧 常用命令

### 环境管理

```bash
# 激活环境
conda activate buybuy

# 退出环境
conda deactivate

# 查看所有环境
conda env list

# 删除环境（如果需要重新创建）
conda env remove -n buybuy
```

### 项目运行

```bash
# 确保在项目目录且已激活环境
cd E:\buybuy
conda activate buybuy

# 启动开发服务器
python manage.py runserver

# 使用其他端口
python manage.py runserver 8001
```

### 数据库操作

```bash
# 创建迁移
python manage.py makemigrations

# 执行迁移
python manage.py migrate

# 查看迁移状态
python manage.py showmigrations

# 创建管理员
python manage.py createsuperuser
```

---

## 🎯 Anaconda 专用启动脚本

我为您创建了 Anaconda 专用的启动脚本：

### Windows - 使用 `start_anaconda.bat`

直接双击运行，或在 Anaconda Prompt 中：
```bash
start_anaconda.bat
```

---

## ⚠️ 常见问题

### Q1: 提示找不到 conda 命令
**解决**：
- 使用 "Anaconda Prompt" 而不是普通的 CMD
- 或者将 Anaconda 添加到系统 PATH

### Q2: pip 安装慢或失败
**解决**：使用国内镜像源
```bash
# 临时使用
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 或
pip install Django==4.2.7 -i https://mirrors.aliyun.com/pypi/simple/
```

### Q3: Pillow 安装失败
**解决**：Anaconda 环境下可以用 conda 安装
```bash
conda install pillow
# 然后安装其他包
pip install Django==4.2.7
pip install django-crispy-forms==2.1
pip install crispy-bootstrap5==1.0.0
pip install python-decouple==3.8
```

### Q4: 端口 8000 被占用
**解决**：使用其他端口
```bash
python manage.py runserver 8001
```

### Q5: 数据库迁移错误
**解决**：删除数据库文件重新创建
```bash
# 删除 db.sqlite3 文件
del db.sqlite3  # Windows
# rm db.sqlite3  # Linux/Mac

# 重新迁移
python manage.py makemigrations
python manage.py migrate
```

---

## 📊 依赖包说明

| 包名 | 版本 | 用途 |
|------|------|------|
| Django | 4.2.7 | Web 框架 |
| Pillow | 10.1.0 | 图片处理 |
| django-crispy-forms | 2.1 | 表单美化 |
| crispy-bootstrap5 | 1.0.0 | Bootstrap 5 支持 |
| python-decouple | 3.8 | 配置管理 |

---

## 🚀 完整流程总结

```bash
# 1️⃣ 打开 Anaconda Prompt

# 2️⃣ 进入项目目录
cd E:\buybuy

# 3️⃣ 创建并激活环境
conda create -n buybuy python=3.10 -y
conda activate buybuy

# 4️⃣ 安装依赖
pip install -r requirements.txt

# 5️⃣ 数据库迁移
python manage.py makemigrations
python manage.py migrate

# 6️⃣ 创建管理员
python manage.py createsuperuser

# 7️⃣ 添加示例数据（可选）
python manage.py shell < create_sample_data.py

# 8️⃣ 启动服务器
python manage.py runserver

# 9️⃣ 访问网站
# 浏览器打开: http://127.0.0.1:8000/
```

---

## 💡 下次启动

以后每次运行项目，只需要：

```bash
# 1. 打开 Anaconda Prompt
# 2. 进入项目目录
cd E:\buybuy

# 3. 激活环境
conda activate buybuy

# 4. 启动服务器
python manage.py runserver
```

或者直接运行 `start_anaconda.bat` 脚本！

---

## 🎓 Anaconda 优势

使用 Anaconda 的好处：
- ✅ 环境隔离，不影响其他项目
- ✅ 包管理更方便
- ✅ 支持科学计算库
- ✅ 适合数据分析和机器学习扩展

---

祝您配置顺利！🎉

