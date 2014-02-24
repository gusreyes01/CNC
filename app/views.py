from django.shortcuts import render, render_to_response
from django.template import RequestContext
# Create your views here.

def home(request):
	return render_to_response('index.html',{}, context_instance=RequestContext(request))

def horizontal(request):
	return render_to_response('horizontal.html',{}, context_instance=RequestContext(request))

def vertical(request):
	return render_to_response('vertical.html',{}, context_instance=RequestContext(request))

def vertical_V1(request):
	return render_to_response('vertical_V1.html',{}, context_instance=RequestContext(request))