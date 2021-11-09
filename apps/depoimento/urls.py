from django.urls import path
from .views import DepoimentoView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', DepoimentoView.as_view(), name='depoimento')
]
