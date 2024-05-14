from django.db import models


class DepartmentCategory(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

    class Meta:
        db_table = 'departmentcategory'
        verbose_name = 'Department Category'
        verbose_name_plural = 'DepartmentCategory'


class Department(models.Model):
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    category_name = models.ForeignKey(DepartmentCategory, related_name='departments_uz', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/image')
    name_cafedra_uz = models.CharField(max_length=255)
    name_cafedra_ru = models.CharField(max_length=255)
    vedio = models.URLField(null=True, blank=True)
    description1_uz = models.CharField(max_length=255, null=True, blank=True)
    description1_ru = models.CharField(max_length=255, null=True, blank=True)
    description2_uz = models.CharField(max_length=255, null=True, blank=True)
    description2_ru = models.CharField(max_length=255, null=True, blank=True)
    description3_uz = models.CharField(max_length=255, null=True, blank=True)
    description3_ru = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name_uz

    class Meta:
        db_table = 'department'
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

