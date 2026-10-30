from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from reports.models import Report as reportAppReportClassModel
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash


def update_password(request):
    user = request.user
    if request.method == "GET":
        return render(request, "updatePassword.html")
    elif request.method == "POST":
        old_pass = request.POST.get("oldPassworD")
        new_pass = request.POST.get("newPsswoRD")
        confirm_pass = request.POST.get("confirmPassWORD")

        if not request.user.check_password(old_pass):
            return render(
                request,
                "updatePassword.html",
                {"old_password_not_matched": "Current password does not matched"},
            )

        if not new_pass:
            return render(
                request,
                "updatePassword.html",
                {"password_length_error": "New password is empty."},
            )

        if len(new_pass) < 5:
            return render(
                request,
                "updatePassword.html",
                {
                    "password_length_error": "Password length is less then five characters."
                },
            )

        if new_pass != confirm_pass:
            return render(
                request,
                "updatePassword.html",
                {"new_confirm_password_not_matched": "Password not matched"},
            )

        user.set_password(new_pass)
        user.save()
        update_session_auth_hash(request, user)
        messages.success(request, "Password updated successfully!")
        return render(request, "userProfile.html")


def editProfile(request):
    user = request.user
    if request.method == "GET":
        return render(request, "editProfile.html")
    elif request.method == "POST":
        fname = request.POST.get("first_namE")
        lname = request.POST.get("last_namE")
        userName = request.POST.get("usernaME")
        eMail = request.POST.get("emaiL")

        if User.objects.filter(username=userName).exclude(id=user.id).exists():
            return render(
                request,
                "editProfile.html",
                {"error_username": "This username already taken"},
            )

        if User.objects.filter(email=eMail).exclude(id=user.id).exists():
            return render(
                request, "editProfile.html", {"error_email": "This email already taken"}
            )

        user.first_name = fname
        user.last_name = lname
        user.username = userName
        user.email = eMail

        user.save()
        messages.success(request, "Profile updated successfully!")

        return redirect("myProfilePage")


def userProfile(request):
    myReports = reportAppReportClassModel.objects.filter(user=request.user).order_by(
        "-create_date"
    )
    totalReports = myReports.count()
    pending = myReports.filter(status="pending").count()
    inProgress = myReports.filter(status="in_progress").count()
    resolveD = myReports.filter(status="ressolved").count()
    return render(
        request,
        "userProfile.html",
        {
            "myAllReports": myReports,
            "totalReports": totalReports,
            "pending": pending,
            "inProgress": inProgress,
            "resolved": resolveD,
        },
    )


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
