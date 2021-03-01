from django.contrib import admin
from .models import *
# Register your models here.

'''class StockAdmin(admin.ModelAdmin):
   list_display = ['category', 'item_name', 'quantity']
   list_filter = ['category']
   search_fields = ['category', 'item_name']'''


admin.site.register(Contact)
admin.site.register(Message)
admin.site.register(To)