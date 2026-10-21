from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.


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
            context['password_not_matched']="Password don't match"
            return render(
                request,"registration.html",context
            )
        
        elif User.objects.filter(username=user_name).exists():
            context['username_exist']="Username already taken"
            return render(
                request, "registration.html",context
               
            )
        elif User.objects.filter(email=emailAddress).exists():
            context['email_exist']="Email already registered"
            return render(
                request, "registration.html",context
            )
        
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
