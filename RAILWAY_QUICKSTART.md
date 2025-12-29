# 🚂 Railway 5分钟快速部署

## 🎯 超简化版本（跟着做就行）

### 第1步：安装部署工具（2分钟）

在 Anaconda Prompt 中：

```bash
cd E:\buybuy
conda activate buybuy

pip install gunicorn whitenoise dj-database-url psycopg2-binary
```

等待安装完成...

---

### 第2步：准备 GitHub（3分钟）

#### A. 安装 Git

1. 下载 Git：https://git-scm.com/download/win
2. 双击安装，一路下一步

#### B. 配置 Git

在 Anaconda Prompt：

```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱@example.com"
```

#### C. 上传代码

```bash
# 在项目目录
cd E:\buybuy

# 初始化
git init

# 添加文件
git add .

# 提交
git commit -m "First commit"
```

#### D. 创建 GitHub 仓库

1. 访问 https://github.com/
2. 注册/登录
3. 点击右上角 "+" → "New repository"
4. 仓库名：`buybuy`
5. 选择 **Public**
6. 点 "Create repository"

#### E. 推送代码

GitHub 会显示命令，复制运行：

```bash
git remote add origin https://github.com/你的用户名/buybuy.git
git branch -M main
git push -u origin main
```

可能需要输入 GitHub 用户名和密码。

---

### 第3步：Railway 部署（1分钟）

#### A. 注册 Railway

1. 访问 https://railway.app/
2. 点 "Login" → "Login with GitHub"
3. 授权 Railway

#### B. 部署

1. 点 "New Project"
2. 选 "Deploy from GitHub repo"
3. 选 `buybuy`
4. 等待部署...

#### C. 添加数据库

1. 在项目中点 "+ New"
2. 选 "Database" → "Add PostgreSQL"
3. 等待创建...

#### D. 配置环境变量

1. 点您的应用
2. 点 "Variables"
3. 添加：

```
RAILWAY_ENVIRONMENT = production
SECRET_KEY = (运行下面命令生成)
```

生成 SECRET_KEY：
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

复制输出的密钥粘贴到 Railway。

#### E. 运行数据库迁移

安装 Railway CLI：

**方法1**（需要 Node.js）：
```bash
npm install -g @railway/cli
```

**方法2**（直接下载）：
https://docs.railway.app/develop/cli

然后运行：
```bash
railway login
railway link
railway run python manage.py migrate
railway run python manage.py createsuperuser
```

#### F. 获取网址

1. 在 Railway 项目中点您的应用
2. 点 "Settings"
3. 找到 "Domains"
4. 点 "Generate Domain"
5. 复制网址！

---

## 🎉 完成！

访问您的网址：`https://xxx.up.railway.app`

管理后台：`https://xxx.up.railway.app/admin`

---

## ❓ 遇到问题？

### 问题1：Railway 部署失败

**看日志**：
- Railway 项目 → "Deployments"
- 点击失败的部署查看错误

### 问题2：无法创建管理员

**使用 Railway 控制台**：
1. Railway 项目 → 点应用
2. 右上角 "..." → "Shell"
3. 输入：
```bash
python manage.py createsuperuser
```

### 问题3：没有 Node.js 无法装 Railway CLI

**直接在 Railway 网站操作**：
- 不用 CLI 也可以
- 在 Railway Settings 中配置
- 数据库会自动迁移

### 问题4：Git 推送需要密码

**使用 Personal Access Token**：
1. GitHub → Settings → Developer settings
2. Personal access tokens → Tokens (classic)
3. Generate new token
4. 复制 token
5. 推送时用 token 做密码

---

## 🔄 以后更新网站

超简单：

```bash
git add .
git commit -m "更新内容"
git push
```

Railway 自动重新部署！

---

## 💰 费用

- ✅ 免费 $5/月 额度
- ✅ 免费数据库
- ✅ 免费 HTTPS
- ✅ 足够小型网站使用

---

## 📱 访问测试

部署完成后测试：

1. ✅ 访问首页
2. ✅ 浏览商品
3. ✅ 登录后台（/admin）
4. ✅ 添加商品测试

---

需要帮助？查看 **RAILWAY_DEPLOY.md** 详细版！

