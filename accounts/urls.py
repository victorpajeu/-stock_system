from django.urls import path
from accounts.views import Dashboard, Login

app_name = 'accounts'

urlpatterns = [
    path('home/', Dashboard.as_view(), name='dashboard'),
    path('login/', Login.as_view(), name='login'),
]