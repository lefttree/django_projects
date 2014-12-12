from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context
from django.contrib.flatpages.models import FlatPage
from django.shortcuts import render_to_response

def search(request):
    query = request.GET['q']
    '''
    #(1) load the template
    results = FlatPage.objects.filter(content__icontains=query)
    template = loader.get_template('search/search.html')
    #(2) create a context
    context = Context({'query': query, 'results': results})
    #(3) render the html
    response = template.render(context)
    '''
    #use shortcut to handle step 1,2,3
    context_dic = {}
    context_dic['query'] = query
    context_dic['results'] = FlatPage.objects.filter(content__icontains=query)
    return render_to_response('search/search.html', context_dic)
