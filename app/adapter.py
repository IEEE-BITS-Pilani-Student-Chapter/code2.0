from django.contrib.auth.models import User
from django.shortcuts import HttpResponse,redirect
from allauth.account.models import EmailAddress
from allauth.exceptions import ImmediateHttpResponse
from allauth.socialaccount.signals import pre_social_login
from allauth.account.utils import perform_login
from django.dispatch import receiver
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter  
import django.contrib.messages as messages

class MySocialAccount(DefaultSocialAccountAdapter):
    login_bits_mail = 1
    def pre_social_login(self, request, sociallogin): 
        user = sociallogin.user
        if not user.email.split('@')[1] == "pilani.bits-pilani.ac.in":
            context = {}
            context['login_bits_mail'] = int(self.login_bits_mail)
            self.login_bits_mail = 0
            messages.add_message(request, messages.INFO, self.login_bits_mail)
            raise ImmediateHttpResponse(redirect('/'))
        if user.id:  
            return          
        try:
            user = User.objects.get(email=user.email)  # if user exists, connect the account to the existing account and login
            sociallogin.connect(request, user)
        except User.DoesNotExist:
            pass