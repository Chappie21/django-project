from rest_framework.serializers import ModelSerializer
from ..models import Dev

class DevSerializer(ModelSerializer):
    class Meta:
        model = Dev
        # fields = '__all__'
        fields = ['id', 'first_name', 'last_name', 'email', 'age', 'country']
        read_only = ['id', 'created_at', 'updated_at']