from django.urls import path, include
from .views import UserCreateView, AdminAuthorView


urlpatterns = [
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('change_status_author/', AdminAuthorView.as_view(), name='admin-author'),

]
