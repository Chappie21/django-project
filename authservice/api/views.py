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
from .serializers import RegisterSerializaer
from drf_yasg.utils import swagger_auto_schema

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

@api_view(['POST'])
@swagger_auto_schema(
    operation_description="register new user",
    request_body=RegisterSerializaer,
    responses={400: 'Bad request', 201: 'User registered successfully'}
)
def register(requets):
    
    # verify form data
    registerSer = RegisterSerializaer(data=requets.data)

    # verify all form is correct and not have errors
    if not registerSer.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST, data=registerSer.errors)

    # register user
    user = registerSer.save()

    # generate JWT token
    token = RefreshToken.for_user(user)
    
    return Response(
        status=status.HTTP_201_CREATED,
        data = {
            'message': 'User registered successfully',
            'refresh': str(token),
            'token': str(token.access_token),
            'user': registerSer.data
        }
    )


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def check_token(request):
    return Response(status=status.HTTP_200_OK, data={ 'message': f'Valid for {request.user.email}'})