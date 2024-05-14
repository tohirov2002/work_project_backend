from django.db import models


class DoctorCategory(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

    class Meta:
        db_table = 'doctorcategory'
        verbose_name = 'Doctor Category'
        verbose_name_plural = 'DoctorCategory'


class Doctor(models.Model):
    name = models.CharField(max_length=255)
    category_name = models.ForeignKey(DoctorCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/image')
    specialty_uz = models.CharField(max_length=255)
    specialty_ru = models.CharField(max_length=255)
    vedio = models.URLField(null=True, blank=True)
    education = models.CharField(max_length=255)
    experience1_uz = models.CharField(max_length=255, null=True, blank=True)
    experience1_ru = models.CharField(max_length=255, null=True, blank=True)
    experience2_uz = models.CharField(max_length=255, null=True, blank=True)
    experience2_ru = models.CharField(max_length=255, null=True, blank=True)
    experience3_uz = models.CharField(max_length=255, null=True, blank=True)
    experience3_ru = models.CharField(max_length=255, null=True, blank=True)
    experience4_uz = models.CharField(max_length=255, null=True, blank=True)
    experience4_ru = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'doctor'
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'

