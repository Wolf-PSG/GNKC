from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):

    levelOptions = (
        ('1', 'Level 1'),
        ('2', 'Level 2'),
        ('3', 'Level 3'),
        ('4', 'Level 4'),
        ('5', 'Level 5'),
        ('6', 'Level 6'),
        ('G', 'GCSE'),
        ('AS', 'AS-Level'),
        ('A', 'A-Level')
    )

    teacherID = models.AutoField(primary_key=True)
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    level = models.CharField(max_length=2, choices=levelOptions)

    def __str__(self):
        return str(self.user)
