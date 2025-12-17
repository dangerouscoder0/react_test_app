from django.urls import path
from .views import hello_world

urlpatterns = [
    path('', hello_world, name='hello_world'), # This matches the base URL of the app
]
