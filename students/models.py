from django.contrib.auth.models import User
from django.db import models
from django.forms.fields import ChoiceField

from teachers.models import Teacher


class Students(models.Model):

  levelOptions = (
	  ('1', 'Level 1'),
	  ('2', 'Level 2'),
	  ('3', 'Level 3'),
	  ('4', 'Level 4'),
	  ('5', 'Level 5'),
	  ('6', 'Level 6'),
	  ('7', 'GCSE'),
	  ('8', 'AS-Level'),
	  ('9', 'A-Level')
  )

  classOptions = (
      ('1', 'Sat AM'),
   	  ('2', 'Sat PM'),
   	  ('3', 'Sun AM'),
   	  ('4', 'Sun PM'),
  )


  studentID = models.AutoField(primary_key=True)
  user = models.OneToOneField(
	  User, null=True, blank=True, on_delete=models.CASCADE)
  teacher = models.OneToOneField(
	  Teacher, null=True, blank=True, on_delete=models.CASCADE)
  level = models.CharField(max_length=2, choices=levelOptions, default=1)
  classes = models.CharField(max_length=2, choices=classOptions, default=1)
  def __str__(self):
	  return str(self.user)
