from re import template
from django.views.generic import TemplateView

# Create your views here.


class ModelView(TemplateView):
    template_name = "model.html"


class ProjectView(TemplateView):
    template_name = "projects.html"


class QualiView(TemplateView):
    template_name = "qualifications.html"


class CurView(TemplateView):
    template_name = "curriculum.html"
