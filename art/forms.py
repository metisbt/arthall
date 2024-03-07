from django import forms
from art.models import Creation, Exhibition, Teaching, RegisterExhibition
from captcha.fields import CaptchaField

class CreationForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Creation
        fields = ['author', 'title', 'category', 'image']

class TeachtForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Teaching
        fields = ['author', 'name', 'subject', 'category', 'date']

class ExhibitionForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Exhibition
        fields = ['author', 'name', 'category', 'date']

class RegisterExhibitionForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = RegisterExhibition
        fields = ['author', 'name']