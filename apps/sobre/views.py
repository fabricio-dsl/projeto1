from django.shortcuts import render

# Create your views here.

from django.views.generic import(
    TemplateView
)


class SobreView(TemplateView):
    template_name = "sobre/sobre.html"

    def get_context_data(self, **kwargs) :
        contex = super(SobreView,self).get_context_data(**kwargs)
        return contex