from django.db import models
from accounts.models import CustomUser

# Create your models here.


class Lesson(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.start_time} - {self.end_time} at {self.location}'
