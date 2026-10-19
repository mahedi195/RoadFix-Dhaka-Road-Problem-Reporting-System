
from django.urls import path,include
from .import views


urlpatterns=[
    #path('report',views.report_list),
    path('',views.report_list),
]