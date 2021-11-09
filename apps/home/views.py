from django.shortcuts import render

# Create your views here.

from django.views.generic.base import(
    TemplateView
)


class HomeView(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs) :
        contex = super(HomeView,self).get_context_data(**kwargs)
        return contex