from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView, View
from django.views.generic.list import ListView

from cv.models import CV


class CvView(View):
    template_name = "cv/%s_detail.html"

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(CV, pk=kwargs['pk'])
        language = 'fr' if not obj.language else obj.language
        template_name = self.template_name % language
        return render(request, template_name, {'obj': obj})


class CvListView(ListView):
    template_name = "cv/list.html"
    model = CV

