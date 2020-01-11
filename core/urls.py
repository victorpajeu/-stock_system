from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.bashboard_or_login, name='dashboard_or_login'),
]