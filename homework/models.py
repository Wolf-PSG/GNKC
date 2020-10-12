from django.db import models
from teachers.models import Teacher


class Homework(models.Model):

  title = models.CharField(max_length=100)
  description = models.CharField(max_length=500)
  due = models.DateField()
  teacher = models.ForeignKey(
      Teacher, unique=False, on_delete=models.CASCADE)

  def __str__(self):
    return self.title
