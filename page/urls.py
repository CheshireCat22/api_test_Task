from django.urls import path, re_path
from .views import get_lists


urlpatterns = [
    re_path("(?:/(?P<path>[a-zA-Z]+)/)?", get_lists)
]
