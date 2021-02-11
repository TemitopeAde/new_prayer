from django.db import models
from django.conf import settings


class PersonDetails(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             blank=True,
                             null=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    age = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    has_paid = models.BooleanField(default=False)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return self.name


class PrayerDetails(models.Model):
    prayer = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ['timestamp']


class PaymentDetails(models.Model):
    email = models.EmailField()
    phone_number = models.IntegerField()
    address = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return self.email


class ScheduleDate(models.Model):
    date = models.DateField()
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return str(self.date)