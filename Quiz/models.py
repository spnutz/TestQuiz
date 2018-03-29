from django.db import models

class Question(models.Model):
    question= models.CharField(max_length=225)
    ans = models.CharField(max_length=225)
    def __str__(self):
        return self.name

