from django.shortcuts import render,HttpResponse

from .models import FeedBack, Job, Test_Detail,Health_Campaign,Contact,Appointment
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'pathology/html/home.html')

def test_details(request):
    testdetail_objects=Test_Detail.objects.all()    
    testdetail_dict={
        "testdetail_key":testdetail_objects
    }

    return render(request,'pathology/html/test_details.html',testdetail_dict)


def feedback(request):
    if request.method=="POST":
        name=request.POST["txtname"]
        email=request.POST["txtemail"]
        feedback=request.POST["txtfeedback"]
        rating=request.POST["cmbrating"]

        f=FeedBack(Name=name,Email=email,Feedbacktext=feedback,Rating=rating)
        f.save()
        print("feedback saved successfully")
        messages.success(request,"Thank you for your feedback")
        return render(request,'pathology/html/feedback.html')


    return render(request,'pathology/html/feedback.html')    



def job(request):
    job_objects=Job.objects.all()
    job_dict={
        "job_data":job_objects
    }  
    return render(request,'pathology/html/job.html',job_dict) 


def health_campaign(request):
    hc_objects=Health_Campaign.objects.all()    
    hc_dict={
        "hc_key":hc_objects
    }

    return render(request,'pathology/html/health_campaign.html',hc_dict)


def ambulance(request):
    return render(request,'pathology/html/ambulance.html')    

def cafeteria(request):
    return render(request,'pathology/html/cafeteria.html')    

def restroom(request):
    return render(request,'pathology/html/restroom.html')    


def doctors(request):
    return render(request,'pathology/html/doctors.html')


def appointment(request):
    if request.method=="GET":
        testdetail_obj=Test_Detail.objects.all()    
        testdetail_dict={
            "testdetail_key":testdetail_obj
             }
        return render(request,'pathology/html/appointment.html',testdetail_dict)


    if request.method =="POST":
        user_name= request.POST["username"]            
        user_email= request.POST["useremail"]
        user_phone= request.POST["userphone"]  
        user_test= request.POST["cmb_tname"]
        user_btype=request.POST["cmb_btype"]
        user_adate=request.POST["usertime"]

        if len(user_phone)>10 or len(user_phone)<10 or int(user_phone)<0:
            messages.error(request,"Please enter a valid phone number")
            return render(request,'pathology/html/appointment.html')

        else:
            a=Appointment(Name=user_name,Phone=user_phone,Email=user_email,Test_Name=user_test,Booking_Type=user_btype,Date=user_adate) #object creation
            a.save()    
            messages.success(request,"Appointment booked successfully.")
            return render(request,'pathology/html/appointment.html')
            
            
            
def contactus(request):
    if request.method=="GET":
        return render(request,'pathology/html/contact.html')


    if request.method =="POST":
        user_name= request.POST["txtname"]  #request.POST.get("txtname")    can  also be used          
        user_email= request.POST["txtemail"]
        user_phone= request.POST["txtphone"]  #request.POST is dictionary and control names are keys here
        user_query= request.POST["txtquery"]

        if len(user_phone)>10 or len(user_phone)<10 or int(user_phone)<0:
          messages.error(request,"Please enter a valid phone number")
          return render(request,'pathology/html/contact.html')

        else:
          c=Contact(Name=user_name,Email=user_email,Phone=user_phone,Your_Query=user_query) #object creation
          c.save()    ###ORM concept  and it will store data into contact table using ORM
          print("Contact saved successfully")
          messages.success(request,"Thankyou for contacting us, we will reach you soon.")
          return render(request,'pathology/html/contact.html')        









        
