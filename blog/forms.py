# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 16:25:26 2019

@author: a.shchitov
"""
from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
