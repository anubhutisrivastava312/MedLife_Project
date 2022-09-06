from django.contrib import admin
from .models import FeedBack, Health_Campaign, Job, Test_Detail,Appointment,Contact

# Register your models here.
admin.site.register(Test_Detail)
admin.site.register(FeedBack)
admin.site.register(Job)
admin.site.register(Health_Campaign)
admin.site.register(Appointment)
admin.site.register(Contact)

