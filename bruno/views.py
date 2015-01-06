from django.shortcuts import render_to_response
from bruno.models import Entry

def entries_index(request):
    return render_to_response('bruno/entry_index.html',
                             { 'entry_list' : Entry.objects.all() })
