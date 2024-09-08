from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, register, ProfileViewSet, UserProfileDetailView

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'profiles', ProfileViewSet, basename='profile')

urlpatterns = [
    path('register/', register, name='register'),
    path('', include(router.urls)),
    path('api/user-profile/', UserProfileDetailView.as_view(), name='user-profile-detail'),
]