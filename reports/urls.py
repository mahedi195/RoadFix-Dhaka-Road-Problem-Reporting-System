from django.urls import path, include
from . import views

urlpatterns = [
    # path('report',views.report_list),
    path("", views.report_list, name="index"),
    #    path('createForm/',views.report_create),
    path("reportForm/", views.report_create, name="report_form"),
    path('report/<int:id>/' ,views.report_details,name='specific_report_details'),
    path('dashboardPage/',views.dashboard, name='Dashboard')

]
