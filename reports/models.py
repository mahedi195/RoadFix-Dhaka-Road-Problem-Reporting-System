from django.db import models
from django.contrib.auth.models import User


class Report(models.Model):

    CATEGORY_CHOICES = [
        ("pothole", "Pothole"),
        ("damaged_road", "Damaged Road"),
        ("waterlogging", "Waterlogging"),
        ("broken_streetlight", "Broken Streetlight"),
        ("other", "Other"),
    ]

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("in_progress", "In Progress"),
        ("resolved", "Resolved"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    #area = models.CharField(max_length=200)

    photo = models.ImageField(upload_to="reportPics/", blank=True, null=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    location=models.CharField(max_length=200)
    road_information=models.CharField(max_length=200)
    landmarks=models.CharField(max_length=300,blank=True)
    additional_details=models.CharField(max_length=500,blank=True)

    def __str__(self):
        return self.title
