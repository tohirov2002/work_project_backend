from rest_framework import viewsets

# Create your views here.
from .models import DoctorCategory, Doctor
from .serializers import DoctorCategorySerializers, DoctorSerializers


class DoctorCategoryView(viewsets.ModelViewSet):
    queryset = DoctorCategory.objects.all()
    serializer_class = DoctorCategorySerializers


class DoctorView(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializers
