from rest_framework import serializers

from .models import DepartmentCategory, Department


class DepartmentCategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = DepartmentCategory
        fields = '__all__'


class DepartmentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = '__all__'


class DepartmentGetSerializers(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(method_name='get_name', read_only=True)

    class Meta:
        model = Department
        fields = ('id', 'name', 'image')

    def get_name(self, obj):
        try:
            lang = self.context['request'].GET['lang']
            if lang == 'ru':
                return obj.name_ru
            return obj.name_uz
        except:
            return obj.name_uz


