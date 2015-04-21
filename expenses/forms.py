from django import forms
from django.forms import ModelForm

from expenses.models import Expense

from datetime import date

class ExpenseForm(ModelForm):
    item = forms.CharField(label='Item', max_length=200)
    price = forms.DecimalField(label='Price', min_value=0, max_digits=8, max_value=999999.99, decimal_places=2)
    date = forms.DateField(initial=date.today)
    class Meta:
        model = Expense
        fields = ['item', 'price', 'date']
