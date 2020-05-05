from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView, View

from cv.models import CV


class CvView(View):
    template_name = "cv/index.html"

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(CV, pk=kwargs['pk'])
        return render(request, self.template_name, {'obj': obj})
