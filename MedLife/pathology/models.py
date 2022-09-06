from django.db import models
from django.utils import timezone

# Create your models here.
class Test_Detail(models.Model):
    Test_name=models.CharField(max_length=100,primary_key=True)
    Charge=models.IntegerField()
    Test_Condition=models.CharField(max_length=100,null=False)


class FeedBack(models.Model):
    Name=models.CharField(max_length=45,null=False)   
    Email=models.CharField(max_length=45,null=False)
    Feedbacktext=models.TextField(null=False)
    Rating=models.IntegerField()
    Date=models.DateField(default=timezone.now)


class Job(models.Model):
    PostName=models.CharField(max_length=50,null=False)    
    NoOfSeats=models.IntegerField(null=False)
    Lastdatetoapply=models.DateField(default=timezone.now)
    Postdate=models.DateField(default=timezone.now)
    Description=models.TextField()



class Health_Campaign(models.Model):
    Campaign_Name=models.CharField(max_length=100,null=False)
    Organizer_Name=models.CharField(max_length=50,null=False)
    Venue=models.CharField(max_length=50,null=False)
    Description=models.CharField(max_length=200,null=False)
    Event_pic=models.FileField(max_length=100,upload_to="pathology/picture",default="")
    Date=models.DateField(default=timezone.now)



class Contact(models.Model):
    Name=models.CharField(max_length=50,null=False)
    Email=models.EmailField(max_length=100,null=True)
    Phone=models.IntegerField(max_length=10,null=False)
    Your_Query=models.TextField(max_length=500,null=False)
    Date=models.DateField(default=timezone.now)


class Appointment(models.Model):
    Name=models.CharField(max_length=50,null=False)
    Phone=models.CharField(max_length=10,null=False)
    Email=models.EmailField(max_length=100,null=True)
    Test_Name=models.CharField(max_length=100,null=False)
    Booking_Type=models.CharField(max_length=100,null=False)
    Date=models.DateField(default=timezone.now)    












    






