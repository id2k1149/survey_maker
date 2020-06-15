from .models import User
from .serializer import UserSerializer
from rest_framework import viewsets


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.prefetch_related('companies', 'groups')
    serializer_class = UserSerializer
