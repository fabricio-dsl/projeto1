from django.shortcuts import render

# Create your views here.

from django.views.generic import(
    TemplateView
)


class DepoimentoView(TemplateView):
    template_name = "depoimento/depoimento.html"

    def get_context_data(self, **kwargs) :
        contex = super(DepoimentoView,self).get_context_data(**kwargs)
        return contex