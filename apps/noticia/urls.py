from django.urls import path
from .views import NoticiaView 
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', NoticiaView.as_view(), name='noticia')

]
