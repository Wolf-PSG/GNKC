from django.db import models
from teachers.models import Teacher


class Homework(models.Model):

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

	classOptions = (
			('1', 'Sat AM'),
		 	  ('2', 'Sat PM'),
		 	  ('3', 'Sun AM'),
		 	  ('4', 'Sun PM'),
	)
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	due = models.DateField()
	classes = models.CharField(max_length=2, choices=classOptions, default=1)
	teacher = models.ForeignKey(
			Teacher, unique=False, on_delete=models.CASCADE)
	level = models.CharField(max_length=2, choices=levelOptions, default=1)

	def __str__(self):
		return self.title
