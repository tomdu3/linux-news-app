from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=100,
        label='',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email address'},),
        required=False,
        help_text='',)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].label = ''
        self.fields['username'].widget.attrs['placeholder'] = 'Username (required)'
        self.fields['username'].help_text = ''

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password (required)'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = ''
        self.fields['password1'].error_messages['invalid'] = 'The password doesn\'t meet the requirements.'
        


        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password (required)'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = ''
        self.fields['password2'].error_messages['password_mismatch'] = 'The two password fields didn\'t match.'


class UserProfileForm(forms.ModelForm):
    password = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False  # Password is optional in the profile form
    )

    confirm_password = forms.CharField(
        label='Confirm Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False  # Confirm password is optional in the profile form
    )

    class Meta:
        model = UserProfile
        fields = ['password', 'confirm_password', 'profile_image']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match. Please try again.")

        return cleaned_data

