from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
	article_id = models.IntegerField(default = 0)
	article_name = models.CharField(max_length = 100)
	description = models.CharField(max_length = 200)
	price = models.DecimalField(max_digits = 10, decimal_places=2)

class Log(models.Model):
	article_id = models.ForeignKey(Article)
	user = models.ForeignKey(User, unique = True)
	date = models.DateTimeField('date-time transfered')
	status = models.BooleanField(default = False)
