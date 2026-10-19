from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def report_list(request):
    return HttpResponse('Hello , Dhqaka road problems')
