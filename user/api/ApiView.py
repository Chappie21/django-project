from rest_framework.views import APIView
from .serializer import UserSerializer
from ..models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser

class UserApiViewListPost(APIView):
    permission_classes = [IsAdminUser]


    def get(self, request):
        print(request.user)
        users = UserSerializer(User.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=users.data)
    
    def post(self, request):
        userData = UserSerializer(data=request.data)

        # validate data
        userData.is_valid(raise_exception=True)

        # register new user
        userData.save()

        return Response(status=status.HTTP_201_CREATED, data={ 'user': userData.data, 'message': 'User Created Successfully'})
    
class UserApiViewGetUpdatedDelete(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        # Validate user exists
        if not User.objects.filter(pk=pk).exists():
            return Response(status=status.HTTP_404_NOT_FOUND, data={ 'message': f'User id:{pk} does not exists' })

        user = UserSerializer(User.objects.get(pk=pk))

        return Response(status=status.HTTP_200_OK, data=user.data)

    def put(self, request, pk:int):

        # Validate user exists
        if not User.objects.filter(pk=pk).exists():
            return Response(status=status.HTTP_404_NOT_FOUND, data={ 'message': f'User id:{pk} does not exists' })

        # get user data
        userData = UserSerializer(User.objects.get(pk=pk), data=request.data)

        # validate data
        userData.is_valid(raise_exception=True)

        # save changes
        userData.save()

        return Response(status=status.HTTP_200_OK, data={ 'user': userData.data, 'message': 'User Updated Successfully' })

    def delete(self, request, pk:int):
    
        # Validate user exists
        if not User.objects.filter(pk=pk).exists():
            return Response(status=status.HTTP_404_NOT_FOUND, data={ 'message': f'User id:{pk} does not exists' })
        
        # if user exists, delete it
        User.objects.get(pk=pk).delete()

        return Response(status=status.HTTP_200_OK, data={ 'message': 'User deleted Successfully' })
