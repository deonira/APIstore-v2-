from rest_framework import status
from rest_framework import viewsets
from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .models import Category, Product, Profile
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, CategorySerializer, ProductSerializer, ProfileSerializer, UserProfileSerializer

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        User.objects.create_user(
            username=serializer.validated_data['username'],
            email=serializer.validated_data['email'],
            password=request.data['password']
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if not Profile.objects.filter(user=user).exists():
            Profile.objects.create(user=user)
        return Profile.objects.filter(user=user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
class UserProfileDetailView(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user
        try:
            profile = Profile.objects.get(user=user)
            return {
                'user': user,
                'profile': profile
            }
        except Profile.DoesNotExist:
            return {
                'user': user,
                'profile': None
            }

class ProductCreateView(APIView):
    @swagger_auto_schema(
        operation_description="Создать новый продукт",
        responses={
            status.HTTP_201_CREATED: openapi.Response('Продукт создан', ProductSerializer),
            status.HTTP_400_BAD_REQUEST: "Ошибка валидации"
        },
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING, description='Название продукта'),
                'description': openapi.Schema(type=openapi.TYPE_STRING, description='Описание продукта'),
                'price': openapi.Schema(type=openapi.TYPE_NUMBER, description='Цена продукта'),
                'category': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID категории продукта'),
            },
            required=['name', 'price', 'category','description'],
            example={
                "name": "Smartphone",
                "description": "Новейший смартфон с множеством функций",
                "price": 499.99,
                "category": 1
            }
        )
    )
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)