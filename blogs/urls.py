from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogLikeView, BlogViewSet

router = DefaultRouter()
router.register(r'blog', BlogViewSet, basename='BlogViewSet')

urlpatterns = [
    path('', include(router.urls)),
    path('like_blog', BlogLikeView.as_view())
]
