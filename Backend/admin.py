from django.contrib import admin
from Backend.models import *
from Backend.api_auth.models import CustomUser
from Backend.api_gestion_centres.models import Centre, Abonnement, Message
#from Backend.api_gestion_centres.models import Abonnement





# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Centre)
admin.site.register(Abonnement)
admin.site.register(Message)

