from urllib.parse import urlparse
from django.urls import path

from . import views

urlpatterns = [
    path('', views.api_view, name='api-view'),
]
