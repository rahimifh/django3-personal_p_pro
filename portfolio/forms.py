from django import forms




class ContactUS (forms.Form):
    full_name = forms.CharField (max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'full_name' }))
    email = forms.CharField (max_length=100, widget =forms.EmailInput(attrs={'class':'form-control', 'placeholder':'email'}))
    phone = forms.CharField (max_length=100, widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'phone'}))
    message = forms.CharField(max_length=1000, widget =forms.Textarea(attrs={'class':'form-control', 'placeholder':'live message'}))
