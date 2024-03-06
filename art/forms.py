from django import forms
from art.models import Creation, Exhibition, Teaching, RegisterExhibition
# from captcha.fields import CaptchaField

class CreationForm(forms.ModelForm):

    class Meta:
        model = Creation
        fields = ['title', 'content', 'image', 'category', 'author', 'status']

class TeachtForm(forms.ModelForm):

    class Meta:
        model = Teaching
        fields = ['userid', 'name', 'subject', 'category', 'date']

class ExhibitionForm(forms.ModelForm):

    class Meta:
        model = Exhibition
        fields = ['userid', 'name', 'category', 'date']

class RegisterExhibitionForm(forms.ModelForm):

    class Meta:
        model = RegisterExhibition
        fields = ['userid', 'name']