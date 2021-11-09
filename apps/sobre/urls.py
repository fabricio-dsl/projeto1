from django.urls import path
from .views import SobreView 
from django.views.generic.base import TemplateView

urlpatterns = [

    path('', SobreView.as_view(), name='sobre')
]
