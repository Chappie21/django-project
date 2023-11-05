from rest_framework.serializers import ModelSerializer
from user.models import User

class AuthSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']