from django.contrib import admin
from . models import bhubaneswarjob

class bhubaneswaradmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phone']

admin.site.register(bhubaneswarjob,bhubaneswaradmin)



