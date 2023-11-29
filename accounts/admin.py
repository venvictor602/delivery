from django.contrib import admin

# Register your models here.
from .models import *
from django.utils.html import format_html
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
  list_display = ('name','email', 'phone', 'contact_date')
  list_display_links = ('name','phone', 'email')
  search_fields = ('name','email', 'phone')
  list_per_page = 25

class QuoteAdmin(admin.ModelAdmin):
  list_display = ('sender_name','sender_origin', 'froms', 'tos','request_date')
  list_display_links = ('sender_name','froms', 'sender_origin')
  search_fields = ('sender_name','sender_origin', 'froms')
  list_per_page = 25

class TrackingAdmin(admin.ModelAdmin):
  list_display = ( 'trackingid','Sender_Name', 'Reciver_Name','Reciver_Email', 'date_created')
  list_display_links = ('trackingid','Sender_Name', 'Reciver_Name')
  search_fields = ('trackingid','Sender_Name', 'Reciver_Name')
  list_per_page = 25


class TimelineAdmin(admin.ModelAdmin):
  list_display = ( 'trackingid', 'Activity','Location', 'date_created')
  list_display_links = ('Activity','trackingid','Location')
  search_fields = ('Activity',)
  list_per_page = 25


admin.site.register(Tracking, TrackingAdmin)
admin.site.register(Timeline, TimelineAdmin)
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Profile)