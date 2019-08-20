"""
file：form.py
author：陈先生
date：2019/8/1822:50
blog:https://chenpb-lu.github.io
"""
from django import forms
from django.forms import widgets

class SearchForm(forms.Form):
    city = forms.CharField(label="城市",widget=widgets.TextInput(attrs={'type':"text", 'class':"area-danxuan form-control", 'placeholder':"选择地点", 'style':'width: 120px',  'value':"长沙", 'data-value':""}))
    time = forms.CharField(label="城市",widget=widgets.TextInput(attrs={'class':"form-control", 'placeholder':"选择日期",'id':"demo", 'readonly':"readonly", 'style':"width: 200px;background-color: white !important;"}))
