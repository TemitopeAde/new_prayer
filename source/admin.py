from django.contrib import admin
from .models import PersonDetails, PrayerDetails, PaymentDetails, ScheduleDate


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('email', 'timestamp', 'user')


class PersonAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'location', 'age')


class PrayerAdmin(admin.ModelAdmin):
    list_display = ('user', 'timestamp')


admin.site.register(PersonDetails, PersonAdmin)
admin.site.register(PrayerDetails, PrayerAdmin)
admin.site.register(PaymentDetails)
admin.site.register(ScheduleDate, ScheduleAdmin)