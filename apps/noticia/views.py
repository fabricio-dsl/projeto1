from django.shortcuts import render

# Create your views here.

from django.views.generic import(
    TemplateView
)


class NoticiaView(TemplateView):
    template_name = "noticia/noticia.html"

    def get_context_data(self, **kwargs) :
        contex = super(NoticiaView,self).get_context_data(**kwargs)
        return contex