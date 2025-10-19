from django.contrib import admin
from .models import MorSh
# Register your models here.

@admin.register(MorSh)
class MorShAdmin(admin.ModelAdmin):
    list_display = ["First_Name",'Last_Name','status']
    list_editable = ["status"]
    raw_id_fields = ["auther"]
    list_filter = ['status']
    search_fields = ['First_Name','Last_Name']
