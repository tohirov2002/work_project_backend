from rest_framework import viewsets

from .models import DepartmentCategory, Department
from .serializers import DepartmentCategorySerializers, DepartmentSerializers, DepartmentGetSerializers
from .permission import IsAdminReadOnly


class DepartmentCategoryView(viewsets.ModelViewSet):
    queryset = DepartmentCategory.objects.all()
    serializer_class = DepartmentCategorySerializers
    permission_classes = [IsAdminReadOnly]


class DepartmentView(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    permission_classes = [IsAdminReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET' and 'pk' not in self.kwargs:
            return DepartmentGetSerializers
        return DepartmentSerializers


