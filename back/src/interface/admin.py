from django.contrib import admin
from .models import Portofolio

@admin.register(Portofolio)
class PortofolioAdmin(admin.ModelAdmin):
    list_display = ("nom", "email", "sujet", "message")


