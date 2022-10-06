from rest_framework.routers import DefaultRouter

from . import views
from django.urls import path, include

from .views import TransferView

# router = DefaultRouter()
# router.register('api/transfer', TransferView)  # ㅓ래

urlpatterns = [
    path('', views.home),
    path('transfer', TransferView.as_view())
]
