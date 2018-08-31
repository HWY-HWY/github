# -*- coding: utf-8 -*-
# @File  : comment_text_form.py
# @Author: 一稚杨
# @Date  : 2018/8/17/017
# @Desc  :


from django import forms
from ckeditor.widgets import CKEditorWidget


class CommentText(forms.Form):
    comment_text = forms.CharField(label='', widget=CKEditorWidget(config_name='comment_ckeditor'))
