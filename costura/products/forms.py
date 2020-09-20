from django import forms
from crispy_forms.helper import FormHelper 
from crispy_forms.layout import Layout, Submit, Row, Column, Button
from crispy_forms.bootstrap import FormActions, PrependedText
from django_extensions.db.fields import AutoSlugField
from .models import Product
from django.db import transaction

class ProductForm(forms.ModelForm):
    class Meta:
        fields = ['__all__']
    name        = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nome do Produto'}))
    #slug        = AutoSlugField("Endereço digital", unique=True, populate_from="name"
    price       = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder':'Preço'}))
    sale_price  = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder':'Preço Promocional'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Descrição do Produto'}))
    weight      = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder':'Peso(kg)'}),required=False)
    in_stock    = forms.BooleanField(widget=forms.CheckboxInput(attrs={'content':'Disponível'}))
    is_active   = forms.BooleanField(widget=forms.CheckboxInput(attrs={'label':'Anúncio Ativo'}))
    stock       = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Quantia em Estoque'}))
    
class CrispyProductForm(ProductForm):
    def __init__(self, *args, **kwargs):
        super(CrispyProductForm,self).__init__(*args, **kwargs)
        self.fields['name'].label = "Nome do Produto"
        self.fields['price'].label = "Preço"
        self.fields['sale_price'].label = "Preço Promocional"
        self.fields['description'].label = "Descrição"
        self.fields['weight'].label = "Peso(kg)"
        self.fields['is_active'].label = "Anúncio Ativo"
        self.fields['stock'].label = "Estoque Inicial"
        
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-8 mb-0'),
                Column('weight', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column(PrependedText('price', 'R$'),css_class='form-group col-md-4 mb-0'),
                Column(PrependedText('sale_price','R$'),css_class='form-group col-md-4 mb-0'),
                Column('stock', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('is_active', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            'description',
            FormActions(
                Submit('submit', 'Adicionar'),
            )
        )
        
    class Meta:
        model = Product
        fields = '__all__'
        
        
        
    @transaction.atomic
    def save(self):
        product = super().save(commit=False)
        product.save()
        return product