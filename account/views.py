from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# Create your views here.


def user_registration(request):
    if request.method=='GET':
        return render(request,'registration.html')
    elif request.method=='POST':
        first_name=request.POST.get('fname')
        last_name=request.POST.get('lname')
        user_name=request.POST.get('username')
        emailAddress=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')

        if password1!=password2:
            return render(request,'registration.html',
                          {
                              'error':'Password doesnnot matched. '
                          })
        elif User.objects.filter(username=user_name).exists():
             return render(request,'registration.html',
                                      {
                                          'error':'Username already taken. '
                                      })
        elif User.objects.filter(email=emailAddress).exists():
                     return render(request,'registration.html',
                                              {
                                                  'error':'Email already taken. '
                                              })
        else:
              user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=user_name,
                    email=emailAddress,
                    password=password1
              )
              print('user created succesfully')
              return redirect('/')
        
        
        
            

