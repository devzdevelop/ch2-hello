from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse


# Create your views here.
def home_page_view(request):
    template_name = '<h1>Hello World</h1>'
    return HttpResponse(template_name)