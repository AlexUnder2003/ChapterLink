from django.urls import path
from .views import register_user

app_name = 'registration'

urlpatterns = [
    path('', register_user, name='register'),
]