from .models import Company, Department
from .serializer import CompanySerializer, DepartmentSerializer
from rest_framework import viewsets


# ViewSets define the view behavior.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
