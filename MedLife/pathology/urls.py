from django.urls import path,include
from .import views

urlpatterns = [
    path("",views.home,name="home"),
    path("test_details/",views.test_details,name="test_details"),
    path("feedback/",views.feedback,name="feedback"),
    path("job/",views.job,name="job"),
    path("health_campaign/",views.health_campaign,name="health_campaign"),
    path("ambulance/",views.ambulance,name="ambulance"),
    path("cafeteria/",views.cafeteria,name="cafeteria"),
    path("restroom/",views.restroom,name="restroom"),
    path("doctors/",views.doctors,name="doctors"),
    path("contactus/",views.contactus,name="contact"),
    path("appointment/",views.appointment,name="appointment"),


    
    
]
