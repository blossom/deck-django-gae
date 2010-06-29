# coding: UTF-8
from django.shortcuts import *
from django.template import RequestContext

def home(request):
    return render_to_response("pages/home.html", locals(), context_instance=RequestContext(request))
