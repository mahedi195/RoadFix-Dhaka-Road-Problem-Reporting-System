from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class report(models.Model):
    title=models.CharField(max_length=500)
    description=models.TextField()
    category=models.CharField(max_length=200)
    area=models.CharField(max_length=200)
    photo=models.ImageField(upload_to='reportPics',blank=True,null=True)
    status=models.CharField(max_length=200,default='pending')
    create_date=models.DateTimeField(auto_now_add=True,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title

