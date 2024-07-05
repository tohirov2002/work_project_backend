from django.db import models

class MessageModel(models.Model):
    ism = models.CharField(max_length=255)
    familiya = models.CharField(max_length=255)
    tel = models.CharField(max_length=20)
    sana = models.DateField()
    sms = models.TextField(blank=True, null=True)
    fayl = models.FileField(upload_to='uploads/messages/', blank=True, null=True)

    def __str__(self):
        return self.ism

    class Meta:
        db_table = 'message'
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        ordering = ['-sana']
        indexes = [
            models.Index(fields=['ism']),
            models.Index(fields=['familiya']),
            models.Index(fields=['tel']),
        ]
