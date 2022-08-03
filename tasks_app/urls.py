from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MyTaskViewSet, UserPerformersTaskViewList


router = DefaultRouter()
router.register('my_tasks', MyTaskViewSet, basename='tasks')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/performers_tasks/', UserPerformersTaskViewList.as_view(), name='user_performers_tasks')
]
