from django.contrib import admin
from idwall.models import WantedPerson

class ListingWantedPerson(admin.ModelAdmin):
    list_display = ('id', 'name' ,'crimes_committed', 'crime_type', 'investigation_status')
    search_fields = ('name',)
    list_editable = ('investigation_status',)
    
admin.site.register(WantedPerson, ListingWantedPerson)