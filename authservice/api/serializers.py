from rest_framework.serializers import ModelSerializer
from user.models import User

class AuthSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

class RegisterSerializaer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        read_only = ['id']

    def create(self, validated_data):
        # set username equal to email
        validated_data['username'] = validated_data['email']
        user = User.objects.create_user(**validated_data)
        return user