"""
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def report_list(request):
    #return HttpResponse('Hello , Dhqaka road problems')
    return render(request,'index.html')

"""

from django.shortcuts import render, redirect
from .models import Report


def report_list(request):
    all_report = Report.objects.all().order_by("-create_date")
    return render(request, "index.html", {"all_report": all_report})


def report_create(request):
    if request.method == "GET":
        return render(request, "report_form.html")
    elif request.method == "POST":
        title = request.POST.get("title")

        description = request.POST.get("further_details", " ")
        category = request.POST.get("category")
        photo = request.FILES.get("uploaded_photo")
        # status=request.POST.get('title')
        # create_date=request.POST.get('title')
        user = request.user if request.user.is_authenticated else None
        location = request.POST.get("location")
        road_information = request.POST.get("road_information")
        landmarks = request.POST.get("nearby_landmark", " ")
        additional_details = request.POST.get("additional_location_details", " ")

        Report.objects.create(
            title=title,
            category=category,
            photo=photo,
            user=user,
            location=location,
            road_information=road_information,
            landmarks=landmarks,
            description=description,
            additional_details=additional_details,
        )

        return redirect("index")


def report_details(request,id):
    report=Report.objects.get(id=id)
    return render(request,'report_details.html',
                  {
                      'report':report
                  })


