from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'layout/dashboard.html'


class Login(TemplateView):
    template_name = 'login/employee-login.html'
