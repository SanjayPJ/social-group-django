from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup(request):

    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            user_form = form.save()
            user_form.set_password(user_form.password)
            user_form.save()
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = UserForm()

    return render(request, "accounts/signup.html", {
        "form" : form,
    })

def sign_in(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                e_message = "ACCOUNT NOT ACTIVE"
                return render(request, "accounts/login.html", {
                    "e_message" : e_message
                })
        else:
            e_message = "INVALID USERNAME OR PASSWORD"
            return render(request, "accounts/login.html", {
                    "e_message" : e_message
                })
    else:
        return render(request, "accounts/login.html")

@login_required
def sign_out(request):
    logout(request)
    return render(request, "accounts/thanks.html")