from django.urls import path

from .views import UserViewCreate

urlpatterns = [
    path('v1/users/', UserViewCreate.as_view(), name='user_create'),
]
