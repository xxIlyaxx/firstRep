from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class QuestionManager(models.Manager):
    def new(self):
        self.order_by('added_at')

    def popular(self):
        self.order_by('rating')


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(blank=True)
    rating = models.IntegerField()
    author = models.OneToOneField(User)
    likes = models.ManyToManyField(User, related_name='+')
    objects = QuestionManager()


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(blank=True)
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    author = models.OneToOneField(User, on_delete=models.CASCADE)

