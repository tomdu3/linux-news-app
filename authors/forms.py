from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import UserProfile
from django import forms
from cloudinary.forms import CloudinaryFileField

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


class UpdateProfileForm(UserChangeForm):
    email = forms.EmailField(
        max_length=100,
        label='Email:',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email address'},),
        required=False,
        help_text='',)

    profile_image = CloudinaryFileField(
        label='Change Profile Image',
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control-file',
        })
    )

    new_password1 = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'New Password (leave blank to keep current password)'
        }),
        required=False
    )

    new_password2 = forms.CharField(
        label='Confirm New Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm New Password'
        }),
        required=False
    )

    class Meta:
        model = User
        fields = ('email', 'profile_image',)