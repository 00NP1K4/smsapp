from django.db import models
import datetime

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50, blank=False)
    number = models.CharField(max_length=50, blank=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name.capitalize()

class Message(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.contact.name.capitalize()

class To(models.Model):
    number = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.number()