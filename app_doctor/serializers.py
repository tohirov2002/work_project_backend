from rest_framework import serializers

from .models import DoctorCategory, Doctor


class DoctorCategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = DoctorCategory
        fields = '__all__'


class DoctorSerializers(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    class Meta:
        model = Doctor
        fields = '__all__'

    def get_category_name(self, obj):
        return obj.category_name.category_name
