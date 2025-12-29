from .cart import Cart


def cart(request):
    """将购物车添加到模板上下文"""
    return {'cart': Cart(request)}

