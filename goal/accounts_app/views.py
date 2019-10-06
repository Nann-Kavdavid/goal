from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from accounts_app.forms import RegistrationForm


def index(request, sign_up_form=None, login_form=None):
    sign_up_form = sign_up_form or RegistrationForm()
    login_form = login_form or AuthenticationForm()
    context = {'sign_up_form': sign_up_form,
               'login_form': login_form,
               }

    return render(request, template_name='home.html', context=context)


class UserSignUpView(CreateView):
    form_class = RegistrationForm
    template_name = 'home.html'
    success_url = '/accounts'

    def get_absolute_url(self):
        return reverse_lazy("signup")

    def get_context_data(self, **kwargs):
        context = super(UserSignUpView, self).get_context_data(**kwargs)
        context['sign_up_form'] = context['form']
        context['login_form'] = AuthenticationForm()
        return context

    def form_invalid(self, form):
        return index(self.request, sign_up_form=form)


class UserLoginView(auth_views.LoginView):
    template_name = 'home.html'
    success_url = '/blog'

    def get_context_data(self, **kwargs):
        context = super(UserLoginView, self).get_context_data(**kwargs)
        context['login_form'] = context['form']
        context['sign_up_form'] = RegistrationForm()
        return context

    def form_invalid(self, form):
        return index(self.request, login_form=form)


