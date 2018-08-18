# -*- coding: utf-8 -*-
# @File  : template_test.py.py
# @Author: 一稚杨
# @Date  : 2018/8/12/012
# @Desc  :

from django import template
from myapp.models import Article

register = template.Library()


@register.simple_tag
def test(pk):
    author = Article.objects.get(pk=pk).author
    if author == 'hwy':
        author = 'up主'
    return author
