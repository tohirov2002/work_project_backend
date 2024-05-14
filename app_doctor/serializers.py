from rest_framework import serializers

from .models import DoctorCategory, Doctor


class DoctorCategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = DoctorCategory
        fields = '__all__'


class DoctorSerializers(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = '__all__'

