from django.contrib import admin
from Backend.models import *
from Backend.api_auth.models import CustomUser
from Backend.api_gestion_centres.models import Centre
from Backend.api_gestion_centres.models import Abonnement
from Backend.api_gestion_centres.models import Message




# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Centre)
admin.site.register(Abonnement)
admin.site.register(Message)

