import os
import random
import string

from django.contrib.auth.views import LoginView
# from users.forms import UserLoginForm
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserLoginForm, UserProfileForm
from users.models import User


class UserLoginView(LoginView):
    """
    Представление авторизация на сайте
    """
    form_class = UserLoginForm
    template_name = 'users/login.html'
    next_page = 'catalog:index'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация на сайте'
        return context


class RegisterView(CreateView):
    """
    Представление регистрации на сайте с формой регистрации
    """
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация на сайте'
        return context


class ProfileView(UpdateView):
    """
    Представление редактирования профиля
    """
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('catalog:index')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование профиля'
        return context
