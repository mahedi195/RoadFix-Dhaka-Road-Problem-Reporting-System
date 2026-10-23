from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

from reports.models import Report as reportAppReportClassModel


def userProfile(request):
    myReports = reportAppReportClassModel.objects.filter(user=request.user).order_by('-create_date')
    return render(request, "userProfile.html", 
                  {
                      "myAllReports": myReports
                   })


def logout_user(request):
    logout(request)
    return redirect("/")


def user_login(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        rememberMe = request.POST.get("rememberMe")

        user = authenticate(request, username=username, password=password)
        context = {"username": username, "message": "Incorrect username or password"}

        if user is None:  # user is not found
            return render(request, "login.html", context)

        elif user is not None:  # user found
            context["message"] = f"Welcome {username}"
            login(request, user)
            if rememberMe:
                request.session.set_expiry(30 * 24 * 60 * 60)
            else:
                request.session.set_expiry(0)
            return redirect("/")


def user_registration(request):
    if request.method == "GET":
        return render(request, "registration.html")
    elif request.method == "POST":
        first_name = request.POST.get("fname")
        last_name = request.POST.get("lname")
        user_name = request.POST.get("username")
        emailAddress = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        context = {
            "fname": first_name,
            "lname": last_name,
            "username": user_name,
            "email": emailAddress,
        }

        if password1 != password2:
            context["password_not_matched"] = "Password don't match"
            return render(request, "registration.html", context)

        elif User.objects.filter(username=user_name).exists():
            context["username_exist"] = "Username already taken"
            return render(request, "registration.html", context)
        elif User.objects.filter(email=emailAddress).exists():
            context["email_exist"] = "Email already registered"
            return render(request, "registration.html", context)

        else:
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=user_name,
                email=emailAddress,
                password=password1,
            )
            print("user created succesfully")
            return redirect("/")
