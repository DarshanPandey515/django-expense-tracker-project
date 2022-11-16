from django import forms
from myapp.models import Transaction,Profile



class AddTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('transaction_name', 'amount', 'transaction_type', )
        widgets = {
            'transaction_name':forms.TextInput(attrs={'class':'rounded-sm px-4 py-3 mt-1 focus:outline-none bg-gray-100 w-full','placeholder':'Transaction Name'}),
            'amount':forms.NumberInput(attrs={'class':'rounded-sm px-4 py-3 mt-1 focus:outline-none bg-gray-100 w-full','placeholder':'Amount'}),
            'transaction_type':forms.Select(attrs={'class':'rounded-sm px-4 py-3 mt-1 focus:outline-none bg-gray-100 w-full'}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'email', 'income','balance', )
        widgets = {
            'name':forms.TextInput(attrs={'class':'rounded-sm px-4 py-3 mt-1 focus:outline-none bg-gray-100 w-full','placeholder':'Your Name'}),
            'email':forms.EmailInput(attrs={'class':'rounded-sm px-4 py-3 mt-1 focus:outline-none bg-gray-100 w-full','placeholder':'Your Email'}),
            'income':forms.NumberInput(attrs={'class':'rounded-sm px-4 py-3 mt-1 focus:outline-none bg-gray-100 w-full'}),
            'balance':forms.NumberInput(attrs={'class':'rounded-sm px-4 py-3 mt-1 focus:outline-none bg-gray-100 w-full'}),
        }