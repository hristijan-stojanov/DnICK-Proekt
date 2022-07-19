from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from .models import korisnik, Test


@csrf_exempt
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            korisni = korisnik(user=request.user, poeni=0)
            korisni.save()
            messages.success(request, "Registration successful.")
            return redirect("homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="main/register.html", context={"register_form": form})


def homepage(request):
    return render(request, "home.html")


@csrf_exempt
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("homepage")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="main/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("homepage")


def course(request):
    return render(request, "StartCurs.html")


def test(request):
    test = Test.objects.all()
    context = {"tests": test}
    print(test[0].answers)
    return render(request, "test.html", context=context)
