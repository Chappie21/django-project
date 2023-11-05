from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from ..models import Dev
from .serializers import DevSerializer

class DevApiView(APIView):

    def get(self, request):
        devs = DevSerializer(Dev.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=devs.data)
    
    def post(seld, request):

        data = DevSerializer(data=request.data)

        # Verify form
        if (not data.is_valid()):
            return Response(status=status.HTTP_400_BAD_REQUEST, data=data.error_messages)

        # Save new dev
        data.save()

        return Response(status=status.HTTP_201_CREATED, data={ 'dev': data.data, 'message': 'New Dev Created Successfully' })
    
class DevViewSet(ViewSet):
    def list(self, request):
        devs = DevSerializer(Dev.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=devs.data)
    
    def create(self, request):
        data = DevSerializer(data=request.data)

        # Verify form
        data.is_valid(raise_exception=True)

        # Save new dev
        data.save()

        return Response(status=status.HTTP_201_CREATED, data={ 'dev': data.data, 'message': 'New Dev Created Successfully' })
    
    def retrieve(self, request, pk:int):
        dev = DevSerializer(Dev.objects.get(pk=pk))
        return Response(status=status.HTTP_200_OK, data=dev.data)

class DevModelViewSet(ModelViewSet):
    queryset = Dev.objects.all()
    serializer_class = DevSerializer
    http_method_names = ['list', 'post']
    permission_classes = [IsAdminUser]