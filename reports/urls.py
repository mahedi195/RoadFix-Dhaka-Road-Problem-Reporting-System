
from django.urls import path,include
from .import views


urlpatterns=[
    path('',views.report_list)
]