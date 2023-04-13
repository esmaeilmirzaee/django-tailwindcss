from django import forms

from .models import ProductModel

input_css_class = 'form-control'


class ProductForm(forms.ModelForm):
    # name = forms.CharField(widget=forms.TextInput(attrs={'class': 'border border-indigo-500 px-4 py-1'}))
    base_fields = ['__all__']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError('Name must be at least 4 characters')
        return name

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Your name'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = input_css_class

        # self.fields['name'].widget.attrs['class'] = 'border border-1 bg-indidog-50 text-indigo-900 rounded'

    class Meta:
        model = ProductModel
        fields = '__all__'


