from django.db import models
from django.utils import timezone



class User(models.Model):
    username = models.CharField(max_length=20)
    email_id = models.EmailField(max_length=30)
    password = models.CharField(max_length=20)
    def __str__(self):
        return 'username'+self.username+'email'+self.email_id


class Questions(models.Model):
    question_id = models.ForeignKey('User', on_delete=models.CASCADE)
    ans = models.ManyToManyField('Answers')
    question = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.question+'answer--'+self.ans
class Answers(models.Model):
    ans_id = models.ForeignKey('User', on_delete=models.CASCADE)
    answer = models.CharField(max_length=200)
    def __str__(self):
        return str(self.answer)
