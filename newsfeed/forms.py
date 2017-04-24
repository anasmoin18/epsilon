# -*- coding: utf-8 -*-

import re
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

class RegistrationForm(forms.Form):

    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs={'required':True, 'max_length':30, 'class': "form-control", 'placeholder': "luke.skywalker"}), label=_("Username"), error_messages={ 'invalid': _("️️️️⚠️ Your user name may contain only letters, numbers and underscores") })
    email = forms.EmailField(widget=forms.TextInput(attrs={'required':True, 'max_length':30, 'class': "form-control", 'placeholder':"luke.s@rebels.io"}), label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'required':True, 'max_length':30, 'render_value':False, 'class': "form-control", 'placeholder':"Use a combination of characters and numerals!"}), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'required':True, 'max_length':30, 'render_value':False, 'class': "form-control", 'placeholder':""}), label=_("Retype Password"))
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(), label="Remember Me?")
    
    def clean(self, request):
        if not self.cleaned_data.get('remember_me'):
            self.request.session.set_expiry(0)

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("⚠️ This username has already been claimed. Maybe try another one?"))

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("⚠️ The passwords did not match."))
        return self.cleaned_data
