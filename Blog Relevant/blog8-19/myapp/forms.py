# -*- coding: utf-8 -*-
# @File  : forms.py
# @Author: 一稚杨
# @Date  : 2018/7/29/029
# @Desc  :
from django import forms
from django.contrib import auth


class LoginForm(forms.Form):
    # 其中attrs为指定对应字段的前端样式，相当于html表单中的class指定样式
    username = forms.CharField(label='用户名', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='密码', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    # 定义clean方法，该方法是Django Form中特定的方法，只要一执行is_valid这个数据检查方法，就会执行clean这个方法
    # 所以用户验证的内容可以放在这个方法里面，验证时只需要验证is_valid通过，则表示用户信息没有问题，可以直接登录
    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = auth.authenticate(username=username, password=password)
        # 判断用户信息
        if user is None:
            # 用户信息错误，返回错误提示信息
            raise forms.ValidationError('用户名或密码错误！')
        else:
            # 用户信息正确
            self.cleaned_data['user'] = user
        return self.cleaned_data
