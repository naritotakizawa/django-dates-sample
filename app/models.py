from django.db import models
from django.utils import timezone


class Post(models.Model):
    """記事。タイトルと公開日だけ持つ"""
    title = models.CharField('タイトル', max_length=200)
    pub_date = models.DateField('公開日', default=timezone.now)
