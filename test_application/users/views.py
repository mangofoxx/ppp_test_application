from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.contrib import messages

from users.forms import UserRegisterForm, UpdateUserProfileForm


class RegisterView(SuccessMessageMixin, CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')
    success_message = "Account created for %(username)s"

    def form_valid(self, form):
        response = super().form_valid(form)
        self.success_message = self.success_message % {'username': form.cleaned_data.get('username')}
        return response


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    next_page = 'profile'


class PatchLogoutView(LogoutView):
    http_method_names = ["get", "post", "options"]

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class UserProfile(LoginRequiredMixin, View):
    redirect_field_name = ''
    login_url = 'login'
    template_name = 'users/profile.html'

    def get(self, request):
        user_form = UpdateUserProfileForm(instance=request.user)
        return self.render_form(request, template_name=self.template_name ,user_form=user_form)

    def post(self, request):
        user_form = UpdateUserProfileForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data.get('username')
            messages.success(request, f'Account updated for {username}')
            return redirect('profile')

        return self.render_form(request, template_name=self.template_name, user_form=user_form)

    @staticmethod
    def render_form(request, template_name, **kwargs):
        context = {}
        for key, value in kwargs.items():
            context.update({key: value})

        return render(request, template_name=template_name, context=context)
