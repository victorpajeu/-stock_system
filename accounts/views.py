from django.views.generic import TemplateView


class Dashboard(TemplateView):
    template_name = 'layout/dashboard.html'


class Login(TemplateView):
    template_name = 'login/employee-login.html'
