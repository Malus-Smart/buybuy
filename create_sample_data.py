"""
创建示例数据的脚本
运行方式: python manage.py shell < create_sample_data.py
或者: python manage.py shell
然后在shell中: exec(open('create_sample_data.py').read())
"""

from shop.models import Category, Product
from decimal import Decimal

print("开始创建示例数据...")

# 创建分类
categories_data = [
    {'name': '电子产品', 'slug': 'electronics'},
    {'name': '服装鞋包', 'slug': 'fashion'},
    {'name': '食品饮料', 'slug': 'food'},
    {'name': '图书音像', 'slug': 'books'},
    {'name': '家居生活', 'slug': 'home'},
]

categories = {}
for cat_data in categories_data:
    category, created = Category.objects.get_or_create(
        slug=cat_data['slug'],
        defaults={'name': cat_data['name']}
    )
    categories[cat_data['slug']] = category
    if created:
        print(f"创建分类: {category.name}")
    else:
        print(f"分类已存在: {category.name}")

# 创建商品
products_data = [
    {
        'category': 'electronics',
        'name': '智能手机',
        'slug': 'smartphone',
        'description': '最新款智能手机，配备高清屏幕和强大处理器',
        'price': Decimal('3999.00'),
        'stock': 50,
    },
    {
        'category': 'electronics',
        'name': '笔记本电脑',
        'slug': 'laptop',
        'description': '轻薄便携，性能强劲的商务笔记本',
        'price': Decimal('5999.00'),
        'stock': 30,
    },
    {
        'category': 'electronics',
        'name': '无线耳机',
        'slug': 'wireless-headphones',
        'description': '降噪功能，音质出色的无线蓝牙耳机',
        'price': Decimal('599.00'),
        'stock': 100,
    },
    {
        'category': 'fashion',
        'name': '休闲T恤',
        'slug': 'casual-tshirt',
        'description': '纯棉材质，舒适透气的休闲T恤',
        'price': Decimal('99.00'),
        'stock': 200,
    },
    {
        'category': 'fashion',
        'name': '运动鞋',
        'slug': 'sports-shoes',
        'description': '专业运动鞋，缓震透气，适合跑步健身',
        'price': Decimal('399.00'),
        'stock': 80,
    },
    {
        'category': 'fashion',
        'name': '牛仔裤',
        'slug': 'jeans',
        'description': '经典款牛仔裤，百搭耐穿',
        'price': Decimal('299.00'),
        'stock': 150,
    },
    {
        'category': 'food',
        'name': '有机燕麦片',
        'slug': 'organic-oats',
        'description': '健康营养的有机燕麦片，早餐首选',
        'price': Decimal('49.00'),
        'stock': 500,
    },
    {
        'category': 'food',
        'name': '坚果礼盒',
        'slug': 'nuts-gift-box',
        'description': '精选多种坚果，健康美味的零食礼盒',
        'price': Decimal('128.00'),
        'stock': 200,
    },
    {
        'category': 'books',
        'name': 'Python编程从入门到实践',
        'slug': 'python-programming-book',
        'description': 'Python编程经典教材，适合初学者',
        'price': Decimal('89.00'),
        'stock': 300,
    },
    {
        'category': 'books',
        'name': 'Django Web开发实战',
        'slug': 'django-web-development',
        'description': '深入讲解Django框架的实战教程',
        'price': Decimal('99.00'),
        'stock': 250,
    },
    {
        'category': 'home',
        'name': '智能台灯',
        'slug': 'smart-desk-lamp',
        'description': '护眼智能台灯，可调节亮度和色温',
        'price': Decimal('199.00'),
        'stock': 120,
    },
    {
        'category': 'home',
        'name': '床上四件套',
        'slug': 'bedding-set',
        'description': '纯棉床上用品四件套，舒适亲肤',
        'price': Decimal('399.00'),
        'stock': 100,
    },
]

for prod_data in products_data:
    category_slug = prod_data.pop('category')
    product, created = Product.objects.get_or_create(
        slug=prod_data['slug'],
        defaults={
            **prod_data,
            'category': categories[category_slug],
            'available': True,
        }
    )
    if created:
        print(f"创建商品: {product.name}")
    else:
        print(f"商品已存在: {product.name}")

print("\n示例数据创建完成！")
print(f"共创建了 {Category.objects.count()} 个分类")
print(f"共创建了 {Product.objects.count()} 个商品")
print("\n现在可以访问网站查看商品了！")

