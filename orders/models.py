from django.db import models
from django.contrib.auth.models import User
from shop.models import Product


class Order(models.Model):
    """订单"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户', null=True, blank=True)
    first_name = models.CharField('名字', max_length=50)
    last_name = models.CharField('姓氏', max_length=50)
    email = models.EmailField('邮箱')
    address = models.CharField('地址', max_length=250)
    postal_code = models.CharField('邮编', max_length=20)
    city = models.CharField('城市', max_length=100)
    created = models.DateTimeField('创建时间', auto_now_add=True)
    updated = models.DateTimeField('更新时间', auto_now=True)
    paid = models.BooleanField('是否支付', default=False)
    
    class Meta:
        ordering = ['-created']
        verbose_name = '订单'
        verbose_name_plural = '订单'
    
    def __str__(self):
        return f'订单 {self.id}'
    
    def get_total_cost(self):
        """计算订单总价"""
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    """订单项"""
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name='订单')
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE, verbose_name='商品')
    price = models.DecimalField('价格', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField('数量', default=1)
    
    class Meta:
        verbose_name = '订单项'
        verbose_name_plural = '订单项'
    
    def __str__(self):
        return str(self.id)
    
    def get_cost(self):
        """计算订单项总价"""
        return self.price * self.quantity

