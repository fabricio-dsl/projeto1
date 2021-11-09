from django.urls import path
from .views import VideoView 
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', VideoView.as_view(), name='video')
]
