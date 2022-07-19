from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class answer(models.Model):
    answer = models.TextField(null=True, blank=True)


class Test(models.Model):
    question = models.TextField(null=True, blank=True)
    answers = models.ManyToManyField("answer", verbose_name="list of answer ")
    correct_answer = models.TextField(null=True, blank=True)


class korisnik(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    poeni = models.IntegerField()

    def __str__(self):
        return self.user.username
