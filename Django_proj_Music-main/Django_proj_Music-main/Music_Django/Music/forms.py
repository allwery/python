from django import forms

from .models import Buying, Buyer


class BuyingForm(forms.ModelForm):
    class Meta:
        model = Buying
        fields = ['buy_date', 'concert', 'buyer', 'place']


class BuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = ['first_name', 'last_name', 'email']