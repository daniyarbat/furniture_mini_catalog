from django import forms

from catalog.models import Product


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман']

    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        if cleaned_data.lower() in self.forbidden_words:
            raise forms.ValidationError('Недопустимое значение имени')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        if cleaned_data.lower() in self.forbidden_words:
            raise forms.ValidationError('Недопустимое значение в описании')
        return cleaned_data
