#coding:utf-8
from django import forms
from models import Category,Page,UserProfile
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
    name=forms.CharField(max_length=128,help_text=u'请输入名字')
    views=forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    likes=forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    slug=forms.CharField(widget=forms.HiddenInput(),required=False)
    class Meta:
        model=Category
        fields=('name',)

class PageForm(forms.ModelForm):
    title=forms.CharField(max_length=128)
    url=forms.URLField(max_length=200)
    views=forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    #在submit之前调用 可以进行数据验证
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        # If url is not empty and doesn't start with 'http://', prepend 'http://'.
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

        return cleaned_data
    class Meta:
        model=Page
        exclude=('category',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')