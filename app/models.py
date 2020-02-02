from django.db import models
from django.conf import settings


class Question(models.Model):
    name = models.CharField(max_length=30)
    text = models.CharField(max_length=600)

    def __str__(self):
        return self.name

class Participant(models.Model):
    name = models.CharField(max_length=50, default="")
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    bits_id = models.CharField(max_length=15, unique=True)
    score = models.IntegerField(default=0)
    start_time = models.TimeField(null=True)
    def __str__(self):
        return self.bits_id

class Solution(models.Model):
    LANG = (
        ['Python', 'Python'],
        ['C', 'C'],
        ['C++', 'C++'],
    )
    user = models.ForeignKey(Participant, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    lang = models.CharField(max_length=10, choices=LANG, default="C++")
    code = models.TextField(default="")

    def __str__(self):
        return self.question
