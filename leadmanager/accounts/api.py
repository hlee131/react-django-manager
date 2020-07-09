from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer

# Register API


class RegisterAPI(generics.GenericAPIView):
    # Class for validation, serializing and deserializing
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        # get_serializer returns serializer instance, then passing data into instance
        serializer = self.get_serializer(data=request.data)
        # Raises ValidationError if not valid
        serializer.is_valid(raise_exception=True)
        # .save() creates new model/object instance with validated data
        # This calls .create()
        user = serializer.save()
        return Response({
            # get_serializer_context returns dict containing 'request', 'view' and 'format' keys by default
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            # Creates new AuthToken unique for user, similar to user creation with User.objects.create()
            "token": AuthToken.objects.create(user)[1]
        })

# Login API


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

# Get User API


class UserAPI(generics.RetrieveAPIView):
    # RetrieveAPIView is read-only with single model instance
    # Only authenticated users have access to view
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
