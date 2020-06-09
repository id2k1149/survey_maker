from .models import User
from rest_framework import serializers


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    companies = serializers.StringRelatedField(many=True)
    groups = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ['email', 'avatar', 'companies', 'groups']
