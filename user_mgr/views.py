# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from user_mgr.forms import UserRegistrationForm, UserLoginForm, UserAccountForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from user_mgr.models import UserAccount
from django.http import HttpResponse
# Create your views here.
def IndexView(request):
    return render(request, 'user_mgr/index.html', {})

# def registerView(request):

#     if request.user.is_authenticated():
#         # messages.success(request, 'Authenticated')
#         return redirect(reverse('timeline:user_timeline', kwargs = {'username':request.user.username}))

#     context = {}
#     form = UserRegistrationForm()
#     context['form'] = form
#     if request.method == "POST":
#         user_reg_form = UserRegistrationForm(data = request.POST)
#         rp = request.POST

#         if User.objects.filter(email = rp['email']).exists():
#             context['user_reg_form'] = user_reg_form
#             messages.info(request, "Sorry this user email has been taken")
#             return redirect(reverse('user_mgr:register'))
#         else:
#             if user_reg_form.is_valid():
#                 # user_reg_form.save()
#                 user = User.objects.create(username = rp['username'], first_name = rp['first_name'], last_name = rp['last_name'], email = rp['email'])
#                 user.set_password(rp['password'])
#                 user.save()

#                 useraccount = UserAccount.objects.create(user = user)
#                 # useraccount.save()

#                 if user:
#                     messages.success(request, "Your account details have been saved.")
#                     print "new user created: %s" %(user.username)
#                     auth_user = authenticate(username = user.username, password = rp['password'])
#                     if auth_user:
#                         logged_in_user = login(request, auth_user)
#                         return redirect(reverse('timeline:user_timeline', kwargs = {'username':request.user.username}))
#                 else:
#                     messages.warning(request, "Sorry something went wrong. Unable to save your records.")
#             else:
#                 context['user_reg_form'] = UserRegistrationForm(data = request)
#                 return render(request, 'user_mgr/register.html', context)

#     return render(request, 'user_mgr/register.html', context)

# def loginView(request):

#     if request.user.is_authenticated():
#         # username = request.user.get_full_name()
#         # messages.success(request, username)
#         return redirect(reverse('newsfeed:user_newsfeed', kwargs = {'username':request.user.username}))
#     context = {}
#     form = UserLoginForm()
#     username = ''
#     auth_user = False
#     context['loginForm'] = form
#     if request.method == "POST":
#         login_form = UserLoginForm(data = request.POST)
#         rp = request.POST

#         if User.objects.filter(email = rp['email']).exists():
#             username = User.objects.get(email = rp['email']).username
#             auth_user = authenticate(username = username, password = rp['password'])
#             if auth_user:
#                 logged_in_user = login(request, auth_user)

#                 if not rp['next'] =="":
#                     return redirect(rp['next'])
#                 else:
#                     return redirect('/')
#                 # return HttpResponse('You have been logged in!')
#                 # return render(request, 'newsfeed/newsfeed.html', {})
#                 # return redirect(reverse('newsfeed:user_newsfeed', kwargs = {'username':request.user.username}))
#             else:
#                 messages.error(request, 'Sorry your email or password is not correct!')
#         else:
#             messages.error(request, "Sorry this email address does not exist")
#             context['loginForm'] = UserLoginForm(data = request.POST)
#     return render(request, 'user_mgr/login.html', context)

# def logoutView(request):
#     logout(request)
#     return redirect(reverse('user_mgr:index'))
