from django.db import models

class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='team/%Y/%m/%d/')
    bio = models.TextField()
    joined_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
