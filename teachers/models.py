from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    teacherID = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user)
