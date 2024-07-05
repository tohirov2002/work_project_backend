from django.db import models


class Department(models.Model):
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/image')
    vedio = models.URLField(null=True, blank=True)
    description1_uz = models.CharField(max_length=255, null=True, blank=True)
    description1_ru = models.CharField(max_length=255, null=True, blank=True)
    description2_uz = models.CharField(max_length=255, null=True, blank=True)
    description2_ru = models.CharField(max_length=255, null=True, blank=True)
    description3_uz = models.CharField(max_length=255, null=True, blank=True)
    description3_ru = models.CharField(max_length=255, null=True, blank=True)
    operation1_uz = models.CharField(max_length=255, null=True, blank=True)
    operation1_ru = models.CharField(max_length=255, null=True, blank=True)
    operation2_uz = models.CharField(max_length=255, null=True, blank=True)
    operation2_ru = models.CharField(max_length=255, null=True, blank=True)
    operation3_uz = models.CharField(max_length=255, null=True, blank=True)
    operation3_ru = models.CharField(max_length=255, null=True, blank=True)
    operation4_uz = models.CharField(max_length=255, null=True, blank=True)
    operation4_ru = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name_uz

    class Meta:
        db_table = 'department'
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

