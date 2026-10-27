
from django.urls  import path
from .import views

urlpatterns=[
    path('registration/',views.user_registration,name='register'),
    path('login/',views.user_login,name='loginPage'),
    path('registration/',views.user_registration,name='registerMe'),
    path('logout/',views.logout_user,name='logoutOption'),
    
    path('myProfile/',views.userProfile,name='myProfilePage'),

    path('editProfile/',views.editProfile,name='editProfile'),
    path('update_password/',views.update_password,name='updatePassowrD')







]

