from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
    #return HttpResponse("Rango says hello world! <a href='/rango/about'>About</a>")
    context = RequestContext(request)
    #a dictionary that maps template variable names with python variables
    context_dict = {'boldmessage': 'I am bold'}
    return render_to_response('rango/index.html', context_dict, context)

def about(request):
    response_str = "This is the about page" + "<a href='/rango'>Rango</a>"
    return HttpResponse(response_str)
