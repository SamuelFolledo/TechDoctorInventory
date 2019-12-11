from django.contrib import admin
from .models import Device, Part


class PartInline(admin.TabularInline): #StackedInLine will have it stack, TabularInLine is cleaner
    model = Part.devices.through #.devices.through is needed for many to many relationship as it needs a model, not just Part model
    extra = 3

class DeviceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        ('Date information', {'fields': ['content'], 'classes': ['collapse']}),
    ]
    inlines = [PartInline] #puts Parts in the same field
    list_display = ('title', 'created', 'was_published_recently') #displays these properties on showing lists of devices
    list_filter = ['created'] #give a choice to filter by date created
    search_fields = ['title'] #search device by device's title

admin.site.register(Device, DeviceAdmin)

# admin.site.register(Choice) #will create another thing, but if we want it in the same line (if they are related)
# then we will want an StackedInLine
