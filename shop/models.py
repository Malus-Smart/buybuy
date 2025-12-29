from django.db import models
from django.urls import reverse


class Category(models.Model):
    """商品分类"""
    name = models.CharField('分类名称', max_length=200)
    slug = models.SlugField('URL标识', max_length=200, unique=True)
    
    class Meta:
        ordering = ['name']
        verbose_name = '分类'
        verbose_name_plural = '分类'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    """商品"""
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='分类')
    name = models.CharField('商品名称', max_length=200)
    slug = models.SlugField('URL标识', max_length=200)
    image = models.ImageField('商品图片', upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField('商品描述', blank=True)
    price = models.DecimalField('价格', max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField('库存', default=0)
    available = models.BooleanField('是否可用', default=True)
    created = models.DateTimeField('创建时间', auto_now_add=True)
    updated = models.DateTimeField('更新时间', auto_now=True)
    
    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]
        verbose_name = '商品'
        verbose_name_plural = '商品'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

