from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views

from core.api.viewsets import AccountViewSet

from core.views import UserCreate

router = routers.SimpleRouter()
router.register('accounts', AccountViewSet, basename='accounts')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', views.obtain_auth_token),
    path('user/add/', UserCreate.as_view()),
]
