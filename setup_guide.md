# BuyBuy 项目设置指南

## 📖 详细安装和配置指南

### 第一步：环境准备

1. **确认 Python 版本**
```bash
python --version
# 应该显示 Python 3.8 或更高版本
```

2. **安装虚拟环境（如果还没有）**
```bash
pip install virtualenv
```

### 第二步：项目设置

1. **创建并激活虚拟环境**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

2. **安装项目依赖**
```bash
pip install -r requirements.txt
```

如果安装过程中遇到问题，可以尝试单独安装：
```bash
pip install Django==4.2.7
pip install Pillow==10.1.0
pip install django-crispy-forms==2.1
pip install crispy-bootstrap5==1.0.0
pip install python-decouple==3.8
```

### 第三步：数据库设置

1. **创建数据库迁移文件**
```bash
python manage.py makemigrations shop
python manage.py makemigrations cart
python manage.py makemigrations orders
```

2. **执行数据库迁移**
```bash
python manage.py migrate
```

3. **创建超级管理员账号**
```bash
python manage.py createsuperuser
```
按提示输入：
- 用户名
- 邮箱（可选）
- 密码（输入两次）

### 第四步：添加测试数据

1. **启动开发服务器**
```bash
python manage.py runserver
```

2. **访问管理后台**
打开浏览器访问: http://127.0.0.1:8000/admin/

3. **登录并添加数据**
- 使用刚才创建的超级管理员账号登录
- 添加几个商品分类（Category）
- 添加一些商品（Product）

### 第五步：测试网站功能

访问 http://127.0.0.1:8000/ 测试以下功能：

1. **浏览商品**
   - 查看商品列表
   - 按分类筛选
   - 使用搜索功能

2. **购物车**
   - 添加商品到购物车
   - 修改商品数量
   - 删除商品

3. **用户功能**
   - 注册新用户
   - 登录/登出
   - 查看个人订单

4. **订单流程**
   - 添加商品到购物车
   - 进入结算页面
   - 填写收货信息
   - 提交订单
   - 查看订单详情

## 🔧 常见问题解决

### 问题1：导入错误
**错误**: `ModuleNotFoundError: No module named 'xxx'`

**解决**:
```bash
pip install -r requirements.txt
```

### 问题2：数据库错误
**错误**: `no such table: xxx`

**解决**:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 问题3：静态文件不显示
**解决**:
```bash
python manage.py collectstatic
```

### 问题4：图片无法上传
**解决**:
确保 `media` 目录存在且有写入权限：
```bash
mkdir media
```

## 📊 管理后台使用指南

### 添加商品分类

1. 登录管理后台
2. 点击 "分类" -> "增加 分类"
3. 填写：
   - 分类名称：例如 "电子产品"
   - URL标识：例如 "electronics"（只能包含字母、数字、连字符和下划线）

### 添加商品

1. 点击 "商品" -> "增加 商品"
2. 填写商品信息：
   - 选择分类
   - 商品名称
   - URL标识（建议用拼音或英文）
   - 上传商品图片
   - 商品描述
   - 价格
   - 库存数量
   - 勾选"是否可用"

### 管理订单

1. 点击 "订单" 查看所有订单
2. 可以查看订单详情、商品信息
3. 可以修改订单的支付状态

## 🚀 进阶配置

### 配置邮件服务

在 `settings.py` 中添加：
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-password'
```

### 使用 PostgreSQL 数据库

1. 安装 psycopg2:
```bash
pip install psycopg2-binary
```

2. 修改 `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'buybuy_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 配置缓存

在 `settings.py` 中添加：
```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}
```

## 🎯 开发建议

1. **代码规范**: 遵循 PEP 8 Python 代码规范
2. **Git 使用**: 经常提交代码，写清楚 commit 信息
3. **测试**: 为关键功能编写单元测试
4. **文档**: 及时更新项目文档

## 📚 学习资源

- [Django 官方文档](https://docs.djangoproject.com/)
- [Bootstrap 5 文档](https://getbootstrap.com/docs/5.3/)
- [Python 教程](https://docs.python.org/zh-cn/3/tutorial/)

## 💡 下一步可以做什么

1. 添加支付功能（支付宝、微信支付）
2. 实现商品评论和评分系统
3. 添加商品推荐功能
4. 实现优惠券和促销活动
5. 添加商品收藏功能
6. 实现用户积分系统
7. 添加多语言支持
8. 优化搜索功能（使用 Elasticsearch）
9. 添加实时聊天客服
10. 实现数据分析和报表功能

祝你使用愉快！🎉

