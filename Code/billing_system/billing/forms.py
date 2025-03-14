from django import forms
from .models import Invoice

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['customer', 'total_amount']
