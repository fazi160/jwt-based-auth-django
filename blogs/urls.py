from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
# router.register(r'sample', SampleAPIView, basename='sample')

urlpatterns = [
    # path('users/', include(router.urls)),
]
