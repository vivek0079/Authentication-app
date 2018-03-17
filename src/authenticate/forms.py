from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout

User = get_user_model()

class UserLoginForm(forms.Form):
    """UserLoginForm definition."""
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}), label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), label='')

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Invalid User name")
            if not user.check_password(password):
                raise forms.ValidationError("Invalid Password")
            if not user.is_active:
                raise forms.ValidationError("User does not exists")
        return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
    """UserRegisterForm definition."""
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}), label='')
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}), label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), label='')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}), label='')
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2',
        ]
    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')        
        if password != password2:
            raise forms.ValidationError("Password do not match")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email already been registered")
        return email
