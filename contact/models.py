from django.db import models

class Contact(models.Model):
    name = models.CharField()
    email = models.EmailField()
    subject = models.CharField()
    message = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    
    
    def __str__(self):
        return self.name
