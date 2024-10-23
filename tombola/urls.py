from django.urls import path
from .views import tombola_view

urlpatterns = [
    path('', tombola_view, name='tombola'),
]
