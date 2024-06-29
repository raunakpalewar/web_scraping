from django.db import models


class NewsScrping(models.Model):
    news_topic=models.CharField(max_length=255,null=True)
    news_description=models.TextField(null=True,blank=True)