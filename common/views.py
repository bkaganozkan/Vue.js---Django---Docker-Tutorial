
from re import A
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.hashers import make_password

from common.authentication import JWTAuthentication
from .serializers import UserSerializer
from core.models import User

# Create your views here.


class RegisterAPIView(APIView):
    def post(self, request):
        data = request.data

        if data['password'] != data['password_confirm']:
            raise exceptions.APIException('Password does not match!')
        data['is_ambassador'] = 'api/ambassador' in request.path

        data['password'] = make_password(password=data['password'])
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginAPIView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()
        if user is None:
            raise exceptions.AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise exceptions.AuthenticationFailed('Incorrect password!')


        scope  = 'ambassador' if 'api/ambassador' in request.path else 'admin'

        if user.is_ambassador and scope == 'admin':
            raise exceptions.AuthenticationFailed('Unauthorized')

        token = JWTAuthentication.generate_jwt(user.id, scope)

        response = Response()

        # httponly=True =>  set to be True, it is only validate on backend, more secure
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'message': 'success'
        }
        return response


class UserAPIView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        data = UserSerializer(user).data

        if 'api/ambassador' in request.path:
            data['revenue'] = user.revenue
        return Response(data)


class LogoutAPIView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response = Response()
        response.delete_cookie(key='jwt')

        response.data = {
            'message' : 'success'
        }

        return response


class ProfileInfoAPIView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


    def put(self, request,pk=None):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class ProfilePasswordAPIView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, pk=None):
        user = request.user
        data = request.data

        if data['password'] != data['password_confirm']:
            raise exceptions.APIException('Password does not match!')

        
        user.set_password(data['password'])
        user.save()
        return Response(UserSerializer(user).data)