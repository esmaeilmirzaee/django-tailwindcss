from django.forms import forms

input_css_class = 'border border-indigo-700 px-4 py-1'


class ProductForm(forms.BaseForm):
    # name = forms.CharField(widget=forms.TextInput(attrs={'class': 'border border-indigo-500 px-4 py-1'}))

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError('Name must be at least 4 characters')
        return name

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.get('name').widget.attrs['placeholder'] = 'Your name'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = input_css_class

    class Meta:
        fields = ['name',]


