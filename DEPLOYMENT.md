# 🌍 BuyBuy 项目部署指南 - 让全球都能访问

## 部署方案对比

### 方案一：国内服务器（推荐国内用户为主）⭐

**优势**：
- ✅ 国内访问速度快
- ✅ 支付宝、微信支付方便接入
- ✅ 中文支持好

**平台推荐**：
1. **阿里云** - https://www.aliyun.com/
2. **腾讯云** - https://cloud.tencent.com/
3. **华为云** - https://www.huaweicloud.com/

**需要**：
- 服务器（ECS）
- 域名 + ICP备案（国内必须）
- 数据库（RDS 或自建）

---

### 方案二：海外服务器（推荐国际用户）

**优势**：
- ✅ 无需备案
- ✅ 国际访问快
- ✅ 部署简单

**平台推荐**：
1. **Heroku** - https://www.heroku.com/ (简单但收费)
2. **Railway** - https://railway.app/ (推荐，有免费额度)
3. **DigitalOcean** - https://www.digitalocean.com/
4. **AWS** - https://aws.amazon.com/
5. **Vercel** (前端) + Railway/Heroku (后端)

---

### 方案三：CDN加速（国内外都快）⭐⭐⭐

使用 CDN 可以让全球访问都快：
- 国内：阿里云 CDN、腾讯云 CDN
- 国际：Cloudflare CDN（免费）

---

## 🚀 快速部署方案（推荐新手）

### A. Railway 部署（最简单，5分钟上线）

#### 准备工作

1. **创建 GitHub 账号**并上传代码
2. **注册 Railway** - https://railway.app/

#### 部署步骤

1. **准备部署文件**

我已经为您创建好了，但需要几个额外文件：

**runtime.txt**（指定 Python 版本）
```
python-3.10.12
```

**Procfile**（启动命令）
```
web: gunicorn buybuy.wsgi --log-file -
```

**安装 gunicorn**
```bash
pip install gunicorn
pip freeze > requirements.txt
```

2. **修改 settings.py**（生产环境配置）

3. **上传到 GitHub**

4. **在 Railway 中**：
   - 点击 "New Project"
   - 选择 "Deploy from GitHub repo"
   - 选择您的项目
   - 自动部署！

---

### B. Heroku 部署（稳定可靠）

#### 步骤

1. **安装 Heroku CLI**
```bash
# Windows
# 下载安装：https://devcenter.heroku.com/articles/heroku-cli
```

2. **登录 Heroku**
```bash
heroku login
```

3. **创建应用**
```bash
heroku create your-app-name
```

4. **部署**
```bash
git push heroku main
```

5. **运行迁移**
```bash
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

---

## 📋 详细部署流程（完整版）

### 第一步：准备服务器

#### 购买服务器

**国内推荐**：
- 阿里云轻量应用服务器（60元/月起）
- 腾讯云轻量应用服务器（50元/月起）

**配置建议**：
- CPU: 2核
- 内存: 2GB
- 系统盘: 40GB
- 操作系统: Ubuntu 20.04 LTS

**海外推荐**：
- DigitalOcean Droplet ($5/月)
- Vultr ($5/月)
- AWS EC2 (免费一年)

---

### 第二步：服务器环境配置

SSH 登录服务器后：

```bash
# 更新系统
sudo apt update
sudo apt upgrade -y

# 安装 Python 和依赖
sudo apt install python3.10 python3.10-venv python3-pip -y
sudo apt install nginx -y
sudo apt install postgresql postgresql-contrib -y

# 安装 Git
sudo apt install git -y
```

---

### 第三步：部署项目

```bash
# 1. 创建项目目录
cd /var/www/
sudo mkdir buybuy
sudo chown $USER:$USER buybuy
cd buybuy

# 2. 克隆项目
git clone your-github-url.git .

# 3. 创建虚拟环境
python3.10 -m venv venv
source venv/bin/activate

# 4. 安装依赖
pip install -r requirements.txt
pip install gunicorn psycopg2-binary

# 5. 配置数据库
sudo -u postgres psql
CREATE DATABASE buybuy_db;
CREATE USER buybuy_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE buybuy_db TO buybuy_user;
\q

# 6. 修改 settings.py（使用 PostgreSQL）

# 7. 运行迁移
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
```

---

### 第四步：配置 Gunicorn

创建 Gunicorn 服务文件：

```bash
sudo nano /etc/systemd/system/gunicorn.service
```

内容：
```ini
[Unit]
Description=gunicorn daemon for buybuy
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/buybuy
ExecStart=/var/www/buybuy/venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/var/www/buybuy/buybuy.sock \
          buybuy.wsgi:application

[Install]
WantedBy=multi-user.target
```

启动服务：
```bash
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
```

---

### 第五步：配置 Nginx

```bash
sudo nano /etc/nginx/sites-available/buybuy
```

内容：
```nginx
server {
    listen 80;
    server_name your-domain.com www.your-domain.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root /var/www/buybuy;
    }
    
    location /media/ {
        root /var/www/buybuy;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/var/www/buybuy/buybuy.sock;
    }
}
```

启用配置：
```bash
sudo ln -s /etc/nginx/sites-available/buybuy /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

---

### 第六步：配置域名

1. **购买域名**
   - 国内：阿里云万网、腾讯云
   - 国际：Namecheap、GoDaddy、Google Domains

2. **DNS 解析**
   - A 记录：指向服务器 IP
   - CNAME 记录：www 指向主域名

3. **国内服务器需要 ICP 备案**（15-20天）

---

### 第七步：配置 HTTPS（SSL证书）

使用 Let's Encrypt 免费证书：

```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d your-domain.com -d www.your-domain.com
```

自动续期：
```bash
sudo certbot renew --dry-run
```

---

## 🔒 生产环境安全配置

修改 `settings.py`：

```python
import os
from decouple import config

# 安全配置
DEBUG = False
SECRET_KEY = config('SECRET_KEY')
ALLOWED_HOSTS = ['your-domain.com', 'www.your-domain.com']

# HTTPS 配置
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# 数据库（PostgreSQL）
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# 静态文件
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

创建 `.env` 文件：
```
SECRET_KEY=your-secret-key-here
DB_NAME=buybuy_db
DB_USER=buybuy_user
DB_PASSWORD=your-password
```

---

## 🌏 CDN 配置（加速全球访问）

### Cloudflare CDN（免费）

1. **注册 Cloudflare** - https://www.cloudflare.com/
2. **添加网站**
3. **更改域名 DNS 到 Cloudflare**
4. **开启 CDN 和 HTTPS**

**优势**：
- ✅ 全球 CDN 加速
- ✅ 免费 SSL 证书
- ✅ DDoS 防护
- ✅ 国内外都能快速访问

---

## 💰 成本估算

### 最低成本方案（学习/测试）
- **Railway/Heroku 免费版**: $0/月
- **域名**: ¥30-50/年

### 小型商业方案
- **服务器**: ¥50-100/月
- **域名**: ¥50/年
- **SSL证书**: 免费（Let's Encrypt）
- **CDN**: 免费（Cloudflare）
- **总计**: ¥600-1200/年

### 中型商业方案
- **服务器**: ¥200-500/月
- **数据库**: ¥100-300/月
- **CDN**: ¥50-200/月
- **对象存储**: ¥20-100/月
- **总计**: ¥4000-13000/年

---

## 📱 移动端适配

网站已经是响应式设计，自动适配手机。

如需独立 APP：
- **iOS**: 使用 WebView 封装
- **Android**: 使用 WebView 封装
- **小程序**: 需要重新开发

---

## 🔧 常用部署命令

```bash
# 更新代码
cd /var/www/buybuy
git pull

# 更新依赖
source venv/bin/activate
pip install -r requirements.txt

# 数据库迁移
python manage.py migrate

# 收集静态文件
python manage.py collectstatic --noinput

# 重启服务
sudo systemctl restart gunicorn
sudo systemctl restart nginx
```

---

## 📊 监控和维护

### 日志查看
```bash
# Gunicorn 日志
sudo journalctl -u gunicorn

# Nginx 日志
sudo tail -f /var/log/nginx/error.log
sudo tail -f /var/log/nginx/access.log
```

### 性能监控
- **Uptime Robot** - 网站可用性监控
- **Google Analytics** - 访问统计
- **Sentry** - 错误追踪

---

## 🎯 推荐方案总结

| 需求 | 推荐方案 | 难度 | 成本 |
|------|---------|------|------|
| 快速上线测试 | Railway/Heroku | ⭐ | 免费 |
| 国内用户为主 | 阿里云/腾讯云 + 备案 | ⭐⭐⭐ | 中 |
| 国际用户为主 | DigitalOcean + Cloudflare | ⭐⭐ | 低 |
| 国内外都要快 | 国内服务器 + Cloudflare CDN | ⭐⭐⭐⭐ | 中高 |

---

需要我详细讲解某个部署方案吗？或者您想用哪种方式部署？

