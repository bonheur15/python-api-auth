from django.urls import path
from .views import PublicEndpoint, PrivateEndpoint, RegisterView

urlpatterns = [
    path('public/', PublicEndpoint.as_view(), name='public_endpoint'),
    path('private/', PrivateEndpoint.as_view(), name='private_endpoint'),
    path('register/', RegisterView.as_view(), name='register'),
]
