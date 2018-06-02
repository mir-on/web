from django.db import models
import django.contrib.auth.models


class QuestionManager(models.Manager):
    def new(self):
        latest_question_list = Question.objects.order_by('added_at')
        return latest_question_list

    def byLikes_key(self, question):
        return len(question.likes.values())

    def popular(self):
        popular_question_list = sorted(Question.objects.all(), key=self.byLikes_key)
        return popular_question_list


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=200)
    text = models.TextField()
    added_at = models.DateField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(django.contrib.auth.models.User, related_name='user_author')
    likes = models.ManyToManyField(django.contrib.auth.models.User, related_name='user_likes')

    def __str__(self):
        return self.title


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField('date published')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(django.contrib.auth.models.User)
