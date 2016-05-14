from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import render, redirect

from .forms import UserLoginForm, UserRegisterForm
# Create your views here.


def login_view(request):
    form = UserLoginForm(request.POST or None)
    title = "Login"
    next_url = request.GET.get('next')
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        if next_url:
            return redirect(next_url)
        return redirect('rate:tables_list')

    context = {
        'form': form,
        'title': title
    }

    return render(request, "log_in.html", context)


def logout_view(request):
    logout(request)
    return redirect('rate:tables_list')


def register_view(request):
    form = UserRegisterForm(request.POST or None)
    title = 'Sign Up'

    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect('rate:tables_list')
    context = {
        'form': form,
        'title': title
    }

    return render(request, "sign_up.html", context)
