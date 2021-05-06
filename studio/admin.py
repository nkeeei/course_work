from django.contrib import admin
from .models import *


class StudioImageInline(admin.TabularInline):
    model = StudioImage
    extra = 0

class StudioServiceInline(admin.TabularInline):
    model = Service
    extra = 0

class EquipmentInline(admin.TabularInline):
    model = Equipment
    extra = 0

class SoundEngineerInline(admin.TabularInline):
    model = SoundEngineer
    extra = 0

class StudioAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Studio._meta.fields]
    inlines = [StudioImageInline, StudioServiceInline, EquipmentInline, SoundEngineerInline]
    class Meta:
        model = Studio
admin.site.register(Studio, StudioAdmin)


class StudioImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in StudioImage._meta.fields]
    class Meta:
        model = StudioImage
admin.site.register(StudioImage, StudioImageAdmin)


class EquipmentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Equipment._meta.fields]
    class Meta:
        model = Equipment
admin.site.register(Equipment, EquipmentAdmin)


class SoundEngineerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SoundEngineer._meta.fields]
    class Meta:
        model = SoundEngineer
admin.site.register(SoundEngineer, SoundEngineerAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Service._meta.fields]
    class Meta:
        model = Service
admin.site.register(Service, ServiceAdmin)


class EventAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Event._meta.fields]
    class Meta:
        model = Event
admin.site.register(Event, EventAdmin)


class StudioSessionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in StudioSession._meta.fields]
    search_fields = ['date']
    class Meta:
        model = StudioSession
admin.site.register(StudioSession, StudioSessionAdmin)




