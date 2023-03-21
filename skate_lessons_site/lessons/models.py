from django.db import models
from accounts.models import CustomUser


class Lesson(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.date} {self.start_time} - {self.end_time} at {self.location}'
