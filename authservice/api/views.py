from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.shortcuts import get_object_or_404
from user.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from user.api.serializer import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

@api_view(['POST'])
def login(request):

    # verify form data
    # authSerializer = AuthSerializer(data=request.data)
    # authSerializer.is_valid(raise_exception=True)

    # get and verify user exists
    user = get_object_or_404(User, email=request.data['email'])

    # verify password match
    if not user.check_password(request.data['password']):
        return Response(status=status.HTTP_400_BAD_REQUEST, data={ 'message': 'Invalid credentials' })
    
    # generate JWT token
    token = RefreshToken.for_user(user)

    # serializer user information
    userData = UserSerializer(instance=user)

    return Response(
        status=status.HTTP_200_OK,
        data={
            'refresh': str(token),
            'token': str(token.access_token),
            'user': userData.data
        }
    )

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def check_token(request):
    return Response(status=status.HTTP_200_OK, data={ 'message': f'Valid for {request.user.email}'})