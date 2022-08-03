from django.urls import path

from .views import UserViewCreate

urlpatterns = [
    path('', UserViewCreate.as_view(), name='user_create'),
]
