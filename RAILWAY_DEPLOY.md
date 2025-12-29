# 🚂 Railway 部署指南 - 5分钟上线

## 📋 Railway 部署优势

- ✅ **完全免费**开始（$5 免费额度/月）
- ✅ **自动 HTTPS** 证书
- ✅ **全球 CDN** 加速
- ✅ **自动部署** - 推送代码即自动更新
- ✅ **无需备案** - 立即上线
- ✅ **PostgreSQL 数据库** 免费包含

---

## 🎯 部署步骤（超详细）

### 第一步：安装部署所需的包

在 Anaconda Prompt 中运行：

```bash
# 确保在项目目录
cd E:\buybuy

# 激活环境
conda activate buybuy

# 安装部署工具
pip install gunicorn==21.2.0
pip install whitenoise==6.6.0
pip install dj-database-url==2.1.0
pip install psycopg2-binary==2.9.9
```

**这些包的作用**：
- `gunicorn` - 生产环境服务器
- `whitenoise` - 静态文件服务
- `dj-database-url` - 数据库URL解析
- `psycopg2-binary` - PostgreSQL 驱动

---

### 第二步：配置生产环境设置

我已经帮您更新了 `requirements.txt`。

现在需要修改 `buybuy/settings.py`，在文件末尾添加生产环境配置：

```python
# 在 settings.py 文件末尾添加

import dj_database_url
import os

# Production settings
if os.environ.get('RAILWAY_ENVIRONMENT'):
    DEBUG = False
    ALLOWED_HOSTS = ['*']  # Railway 会自动配置域名
    
    # 数据库配置（Railway PostgreSQL）
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get('DATABASE_URL'),
            conn_max_age=600
        )
    }
    
    # 静态文件配置
    MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    
    # 安全配置
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
```

---

### 第三步：准备 Git 和 GitHub

#### 1. 安装 Git（如果还没有）

下载安装：https://git-scm.com/download/win

#### 2. 配置 Git

在 Anaconda Prompt 中：

```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"
```

#### 3. 初始化 Git 仓库

```bash
cd E:\buybuy

# 初始化 Git
git init

# 添加所有文件
git add .

# 提交
git commit -m "Initial commit for Railway deployment"
```

#### 4. 创建 GitHub 仓库

1. 访问 https://github.com/
2. 点击右上角 "+" → "New repository"
3. 仓库名：`buybuy`
4. 设为 **Public**（必须）
5. 点击 "Create repository"

#### 5. 推送代码到 GitHub

复制 GitHub 给的命令，类似：

```bash
git remote add origin https://github.com/你的用户名/buybuy.git
git branch -M main
git push -u origin main
```

如果需要登录，使用 GitHub 账号密码或 Personal Access Token。

---

### 第四步：Railway 部署

#### 1. 注册 Railway

访问：https://railway.app/

- 点击 "Login"
- 选择 "Login with GitHub"
- 授权 Railway 访问您的 GitHub

#### 2. 创建新项目

1. 点击 "New Project"
2. 选择 "Deploy from GitHub repo"
3. 选择 `buybuy` 仓库
4. Railway 开始自动部署！

#### 3. 添加 PostgreSQL 数据库

1. 在项目页面，点击 "+ New"
2. 选择 "Database" → "PostgreSQL"
3. 数据库会自动创建并连接到您的应用

#### 4. 配置环境变量

点击您的应用 → "Variables" 标签，添加：

```
RAILWAY_ENVIRONMENT=production
SECRET_KEY=your-random-secret-key-here
```

生成随机 SECRET_KEY：
```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

#### 5. 运行数据库迁移

在 Railway 项目中：

1. 点击您的应用
2. 点击 "Settings" 标签
3. 找到 "Deploy" 部分
4. 添加部署后命令（Deploy Command）：

```bash
python manage.py migrate && python manage.py collectstatic --noinput
```

或者使用 Railway CLI：

```bash
# 安装 Railway CLI
npm i -g @railway/cli

# 登录
railway login

# 连接项目
railway link

# 运行命令
railway run python manage.py migrate
railway run python manage.py createsuperuser
```

#### 6. 获取网站地址

部署完成后：
1. 点击 "Settings" 标签
2. 找到 "Domains"
3. 点击 "Generate Domain"
4. 获得类似：`your-app.up.railway.app` 的域名

---

## 🎉 部署完成！

访问您的网站：`https://your-app.up.railway.app`

---

## 📱 创建管理员账号

使用 Railway CLI：

```bash
railway run python manage.py createsuperuser
```

或者在 Railway 网站上：
1. 点击应用
2. 点击 "Deploy Logs"
3. 可以看到部署日志

---

## 🔄 更新网站（自动部署）

以后只需：

```bash
# 1. 修改代码

# 2. 提交到 Git
git add .
git commit -m "更新说明"
git push

# 3. Railway 自动部署！
```

---

## 🌐 绑定自定义域名（可选）

1. 在 Railway 项目中点击 "Settings"
2. 找到 "Domains"
3. 点击 "Custom Domain"
4. 输入您的域名
5. 按提示配置 DNS

---

## 💰 费用说明

**免费额度**：
- $5 使用额度/月
- 500 小时运行时间
- 100GB 出站流量
- 免费 PostgreSQL 数据库

**足够运行小型网站！**

超出后按使用付费：
- $0.000231/GB-Hour（存储）
- $0.10/GB（流量）

---

## 🐛 常见问题

### Q1: 部署失败
**查看日志**：
- Railway 项目 → "Deployments"
- 点击失败的部署查看错误

### Q2: 数据库连接失败
**检查**：
- PostgreSQL 服务是否已添加
- 环境变量 `DATABASE_URL` 是否存在

### Q3: 静态文件404
**解决**：
```bash
railway run python manage.py collectstatic --noinput
```

### Q4: 管理员登录失败
**创建管理员**：
```bash
railway run python manage.py createsuperuser
```

---

## 📊 监控和管理

在 Railway 控制台可以看到：
- 📈 CPU 和内存使用
- 📊 请求统计
- 📝 实时日志
- 💾 数据库状态

---

## 🔧 Railway CLI 常用命令

```bash
# 查看日志
railway logs

# 运行命令
railway run python manage.py migrate
railway run python manage.py createsuperuser
railway run python manage.py shell

# 查看变量
railway variables

# 连接数据库
railway connect postgres
```

---

## ✅ 部署检查清单

- [ ] 安装部署依赖包
- [ ] 修改 settings.py
- [ ] 创建 .gitignore
- [ ] 推送代码到 GitHub
- [ ] 在 Railway 创建项目
- [ ] 添加 PostgreSQL 数据库
- [ ] 配置环境变量
- [ ] 运行数据库迁移
- [ ] 创建管理员账号
- [ ] 测试网站访问

---

祝您部署成功！🎉

