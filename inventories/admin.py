from django.contrib import admin
from .models import Device, Part


class DeviceInline(admin.TabularInline): #StackedInLine will have it stack, TabularInLine is cleaner
    model = Device.parts.through #.devices.through is needed for many to many relationship as it needs a model, not just Device model
    extra = 3

class PartAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        # ('Date information', {'fields': ['created'], 'classes': ['collapse']}),
        ('Author',           {'fields': ['author']})
    ]
    inlines = [DeviceInline] #puts Devices in the same field
    list_display = ('title', 'created', 'was_published_recently') #displays these properties on showing lists of devices
    list_filter = ['created'] #give a choice to filter by date created
    search_fields = ['title'] #search device by device's title

admin.site.register(Part, PartAdmin)

admin.site.register(Device) #will create another thing, but if we want it in the same line (if they are related)
