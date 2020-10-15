from django import forms
from crispy_forms.helper import FormHelper 
from crispy_forms.layout import Layout, Submit, Row, Column, Button
from crispy_forms.bootstrap import FormActions, PrependedText
from django_extensions.db.fields import AutoSlugField
from .models import Product, Category
from django.db import transaction
from django.utils.safestring import mark_safe
from string import Template
from django.conf import settings

class PicturePreviewWidget(forms.widgets.FileInput):
    def render(self, name, value, attrs=None, **kwargs):
        input_html = super().render(name, value, attrs=None, **kwargs)
        img_html = Template("""<img src="$media$link" style="height:200px;"/>""")
        img_html = mark_safe(img_html.substitute(media=settings.MEDIA_URL, link=value))
        return f'{input_html}{img_html}'

class ProductForm(forms.ModelForm):
    class Meta:
        fields = ['__all__']
        exclude = ('creator',)
    name        = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nome do Produto'}))
    price       = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder':'Preço'}))
    discount_price  = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder':'Preço Promocional'}),required=False)
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Descrição do Produto'}))
    is_active   = forms.BooleanField(widget=forms.CheckboxInput(attrs={'label':'Anúncio Ativo'}))
    stock       = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Quantidade em Estoque'}))
    category    = forms.ModelChoiceField(queryset=Category.objects.all())
    image       = forms.ImageField(widget=PicturePreviewWidget,)

class CrispyProductForm(ProductForm):
    def __init__(self, *args, **kwargs):
        super(CrispyProductForm,self).__init__(*args, **kwargs)
        self.fields['name'].label = "Nome do Produto"
        self.fields['price'].label = "Preço"
        self.fields['discount_price'].label = "Preço Promocional"
        self.fields['description'].label = "Descrição"
        self.fields['is_active'].label = "Anúncio Ativo"
        self.fields['stock'].label = "Estoque Inicial"
        self.fields['category'].label = "Categoria do Produto"
        self.fields['image'].label = "Imagem do Produto"

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-8 mb-0'),
                Column('category', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column(PrependedText('price', 'R$'),css_class='form-group col-md-4 mb-0'),
                Column(PrependedText('discount_price','R$'),css_class='form-group col-md-4 mb-0'),
                Column('stock', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('is_active', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('description', css_class='form-group col-md-7 mb-0'),
                Column('image', css_class='form-group col-md-5 mb-0'),
                css_class='form-row'
            ),
            FormActions(
                Submit('submit', 'Aceitar'),
            )
        )
        
    class Meta:
        model = Product
        exclude = ('creator',)

    @transaction.atomic
    def save(self):
        product = super().save(commit=False)
        product.save()
        return product

class ProductImageForm(forms.ModelForm):
    image = forms.FileField()