from django.forms import ModelForm

from .models import Order


class OrderPostForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['type_order'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['value'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['user'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Order
        fields = ('name', 'user', 'type_order', 'value', 'description')