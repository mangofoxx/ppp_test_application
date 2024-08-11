from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserRegisterForm


class RegisterView(SuccessMessageMixin, CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')
    success_message = "Account created for %(username)s"

    def form_valid(self, form):
        response = super().form_valid(form)
        self.success_message = self.success_message % {'username': form.cleaned_data.get('username')}
        return response
