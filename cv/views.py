from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView, View
from django.views.generic.list import ListView

from cv.models import CV


class CvView(View):
    template_name = "cv/detail.html"

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(CV, pk=kwargs['pk'])
        return render(request, self.template_name, {'obj': obj})


class CvListView(ListView):
    template_name = "cv/list.html"
    model = CV

