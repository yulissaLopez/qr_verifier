from django.urls import path
from .views import verificar_distintivo

urlpatterns = [
    path('verificar/', verificar_distintivo, name='verificar_distintivo'),
]
