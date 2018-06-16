from django.db import models

class Question(models.Model):
    question_text= models.CharField(max_length=225)
    #choice1 = models.CharField(default=0 , max_length=100)
    #choice2 = models.CharField(default=0 , max_length=100)
    #user_ans = models.CharField(default=0, max_length=100)
    ans = models.CharField(default=0,max_length=225)
    #choice_text = models.CharField(default=0,max_length=200)
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice1 = models.CharField(default=0,max_length=200)
    choice2 = models.CharField(default=0,max_length=200)
    #ans = models.CharField(max_length=200)
    vote_T = models.IntegerField(default=0)
    vote_F = models.IntegerField(default=0)



