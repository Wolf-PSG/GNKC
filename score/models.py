from django.db import models
from teachers.models import Teacher
from quiz.models import Quiz


class Score(models.Model):
    score = models.IntegerField()
    quiz = models.ForeignKey(Quiz, unique=False, on_delete=models.CASCADE)
    teacher = models.ForeignKey(
        Teacher, unique=False, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.quiz.title
