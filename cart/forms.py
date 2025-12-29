from django import forms


class CartAddProductForm(forms.Form):
    """添加商品到购物车表单"""
    quantity = forms.IntegerField(
        label='数量',
        min_value=1,
        initial=1,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'style': 'width: 80px;'
        })
    )
    override = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )

