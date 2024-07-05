from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class NewsModel(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    content_uz = models.CharField(max_length=500, null=True, blank=True)
    content_ru = models.CharField(max_length=500, null=True, blank=True)
    description_uz = models.TextField(null=True, blank=True)
    description_ru = models.TextField(null=True, blank=True)
    advice1_uz = models.TextField(null=True, blank=True)
    advice1_ru = models.TextField(null=True, blank=True)
    advice2_uz = models.TextField(null=True, blank=True)
    advice2_ru = models.TextField(null=True, blank=True)
    advice3_uz = models.TextField(null=True, blank=True)
    advice3_ru = models.TextField(null=True, blank=True)
    # author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title_uz

    class Meta:
        db_table = 'news'
        verbose_name = 'News'
        verbose_name_plural = 'News'
