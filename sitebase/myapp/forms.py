from django import forms
from django.contrib.auth.hashers import check_password
from django.contrib.auth.forms import AuthenticationForm

from .models import Account
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()


# class UserUpdateForm(UserChangeForm):
#     class Meta:
#         model = User
#         fields = ["username", "password1", "password2", "email"]


class BrandSearchForm(forms.Form):
    search_keyword = forms.CharField(label='Search Keyword')


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='유효한 이메일을 입력해주세요')

    class Meta:
        model = Account
        fields = ["email", 'username']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field in (
                self.fields['email'], self.fields['username'], self.fields['password1'], self.fields['password2']):
            field.widget.attrs.update({'class': 'form-control'})


from django.contrib.auth.hashers import make_password

class AccountAuthenticationForm(forms.ModelForm):
    # class AccountAuthenticationForm(AuthenticationForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(AccountAuthenticationForm, self).__init__(*args, **kwargs)
        for field in (self.fields['email'], self.fields['password']):
            field.widget.attrs.update({'class': 'form-control'})

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data.get('email')
            password = self.cleaned_data.get('password')
            print(email, password, Account.objects.get(email=email))

            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid Login')

# class AccountUpdateform(forms.ModelForm):
#     """
#       Updating User Info
#     """
#     class Meta:
#         model  = Account
#         fields = ('email', 'username')
#         widgets = {
#                    'email':forms.TextInput(attrs={'class':'form-control'}),
#                    'password':forms.TextInput(attrs={'class':'form-control'}),
#         }
#
#     def __init__(self, *args, **kwargs):
#         """
#           specifying styles to fields
#         """
#         super(AccountUpdateform, self).__init__(*args, **kwargs)
#         for field in (self.fields['email'],self.fields['username']):
#             field.widget.attrs.update({'class': 'form-control '})
#
#     def clean_email(self):
#         if self.is_valid():
#             email = self.cleaned_data['email']
#             try:
#                 account = Account.objects.exclude(pk = self.instance.pk).get(email=email)
#             except Account.DoesNotExist:
#                 return email
#             raise forms.ValidationError("Email '%s' already in use." %email)
#     def clean_username(self):
#         if self.is_valid():
#             username = self.cleaned_data['username']
#             try:
#                 account = Account.objects.exclude(pk = self.instance.pk).get(username=username)
#             except Account.DoesNotExist:
#                 return username
#             raise forms.ValidationError("Username '%s' already in use." % username)
