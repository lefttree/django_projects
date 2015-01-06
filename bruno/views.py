from django.shortcuts import render_to_response
from bruno.models import Entry

def entries_index(request):
    context_dict = {
                        'entry_list': Entry.objects.all()
                    }
    return render_to_response('bruno/entry_index.html',
                             context_dict)


def entry_detail(request, year, month, day, slug):
    #when a URL match the pattern, the named groups will be passed as keyword arguments
    import datetime, time
    #need to know how the function works
    date_stamp = time.strptime(year+month+day, "%Y%b%d")
    pub_date = datetime.date(*date_stamp[:3])
    #look up for the entry
    context_dict = {
                        'entry': Entry.objects.get(pub_date__year=pub_date.year, pub_date__month=pub_date.month, pub_date__day=pub_date.day, slug=slug)
                    }
    return render_to_response('bruno/entry_detail.html', context_dict)

