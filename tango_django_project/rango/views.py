from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from rango.forms import CategoryForm

def index(request):
    #return HttpResponse("Rango says hello world! <a href='/rango/about'>About</a>")
    context = RequestContext(request)
    #a dictionary that maps template variable names with python variables
    context_dict = {'boldmessage': 'I am bold'}
    return render_to_response('rango/index.html', context_dict, context)

def about(request):
    context = RequestContext(request)

    context_dict_about = {'aboutmessage': 'about what'}

    #response_str = "This is the about page" + "<a href='/rango'>Rango</a>"
    return render_to_response('rango/about.html', context_dict_about, context)

def add_category(request):
    #Get the context from the request
    context = RequestContext(request)

    #A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            #save the new category to the database
            form.save(commit=True)

            #now call index() view, user will be shown the homepage
            return index(request)
        else:
            print form.errors
    else:
        #request was not a POST, display the form to enter details
        form = CategoryForm()

    return render_to_response('rango/add_category.html', {'form': form}, context)
