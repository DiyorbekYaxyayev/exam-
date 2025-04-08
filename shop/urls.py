from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet, SubCategoryViewSet, ProductViewSet,
    ProductBySlugView, UserProfileView, RegisterView,
    CommentViewSet, CartViewSet
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubCategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('products/slug/<slug:slug>/', ProductBySlugView.as_view(), name='product-by-slug'),
    path('user/me/', UserProfileView.as_view()),
    path('api/register/', RegisterView.as_view(), name='register'),
]
