from rest_framework import viewsets

from .models import Department
from .serializers import DepartmentSerializers, DepartmentGetSerializers


class DepartmentView(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializers

    def get_serializer_class(self):
        if self.request.method == 'GET' and 'pk' not in self.kwargs:
            return DepartmentGetSerializers
        return DepartmentSerializers


