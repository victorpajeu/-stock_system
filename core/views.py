
from django.shortcuts import render, redirect
from django.urls import reverse


def bashboard_or_login(request):
    if request.user.is_authenticated:
        return redirect(reverse('accounts:dashboard'))
    return redirect(reverse('accounts:login'))
