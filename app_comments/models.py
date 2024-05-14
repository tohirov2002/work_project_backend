from django.db import models

# Create your models here.


class CommentsModel(models.Model):
    description = models.TextField()
    description_ru = models.TextField(default=1)
    image = models.ImageField(upload_to='media/image')
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'comment'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
