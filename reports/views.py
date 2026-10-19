'''
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def report_list(request):
    #return HttpResponse('Hello , Dhqaka road problems')
    return render(request,'index.html')

'''



from django.shortcuts import render
from .models import Report


def report_list(request):
    all_report=Report.objects.all()
    return render(request,'index.html',
                  {
                      'all_report':all_report
                  })


