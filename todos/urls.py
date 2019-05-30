from django.conf.urls import url, path
from . import views

urlpatterns = [
    path("home/", views.index, name='index')
]