from django.db import models
from teachers.models import Teacher


class Quiz(models.Model):
	levelOptions = (
            ('1', 'Level 1'),
         			('2', 'Level 2'),
         			('3', 'Level 3'),
         			('4', 'Level 4'),
         			('5', 'Level 5'),
         			('6', 'Level 6'),
         			('7', 'GCSE'),
         			('8', 'AS-Level'),
         			('9', 'A-Level'),
      					 ('10', 'All'),
        )

	classOptions = (
            ('1', 'Sat AM'),
         			('2', 'Sat PM'),
         			('3', 'Sun AM'),
         			('4', 'Sun PM'),
        				('5', 'All')
        )
	title = models.CharField(max_length=100)
	teacher = models.ForeignKey(
            Teacher, unique=False, on_delete=models.CASCADE)
	classes = models.CharField(
            max_length=2, choices=classOptions, default=1)
	level = models.CharField(max_length=2, choices=levelOptions, default=1)
	image_path = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

	def __str__(self):
		return self.title


class Question(models.Model):
	answerOptions = (
            ('1', 'answer_1'),
            ('2', 'answer_2'),
            ('3', 'answer_3'),
            ('4', 'answer_4'),
        )
	quiz = models.ForeignKey(Quiz, unique=False, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	answer_1 = models.CharField(max_length=50)
	answer_2 = models.CharField(max_length=50)
	answer_3 = models.CharField(max_length=50)
	answer_4 = models.CharField(max_length=50)
	correct_answer = models.CharField(
		max_length=2, choices=answerOptions, default=1)
	image_path = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

	def __str__(self):
		return self.title
