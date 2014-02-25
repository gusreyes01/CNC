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

def vertical_V2(request):
	return render_to_response('vertical_V2.html',{}, context_instance=RequestContext(request))

def vertical_V3(request):
	return render_to_response('vertical_V3.html',{}, context_instance=RequestContext(request))

def vertical_V4(request):
	return render_to_response('vertical_V4.html',{}, context_instance=RequestContext(request))

def horizontal_H1(request):
	return render_to_response('horizontal_H1.html',{}, context_instance=RequestContext(request))

def horizontal_H2(request):
	return render_to_response('horizontal_H2.html',{}, context_instance=RequestContext(request))

def horizontal_H3(request):
	return render_to_response('horizontal_H3.html',{}, context_instance=RequestContext(request))

def horizontal_H4(request):
	return render_to_response('horizontal_H4.html',{}, context_instance=RequestContext(request))