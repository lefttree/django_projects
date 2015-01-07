from django.conf.urls import *
from bruno.models import Entry
from bruno.views import EntryYearArchiveView, EntryMonthArchiveView, EntryWeekArchiveView, entries_index
from django.views.generic.dates import DateDetailView, ArchiveIndexView, YearArchiveView


urlpatterns = patterns('',
    url(r'^$', entries_index, name="entries_index"),
    #url(r'^$', ArchiveIndexView.as_view(model=Entry, date_field="pub_date"), name="entry_index"),
    url(r'^(?P<year>\d{4})/$', EntryYearArchiveView.as_view(), name="entry_year"),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$', EntryMonthArchiveView.as_view(), name="entry_month"),
    url(r'^(?P<year>\d{4})/week/(?P<week>\d+)/$', EntryWeekArchiveView.as_view(), name="entry_week"),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', DateDetailView.as_view(queryset=Entry.objects.all(), date_field='pub_date'), name="entry_detail"),
)
