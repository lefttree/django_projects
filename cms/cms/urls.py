from django.conf.urls import patterns, include, url
import os
SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = os.path.dirname(SETTINGS_DIR)
TINYMCE_PATH = PROJECT_PATH + "/tinymce/js/tinymce"


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from bruno.models import Entry
from bruno.views import EntryYearArchiveView, EntryMonthArchiveView, EntryWeekArchiveView
from django.views.generic.dates import DateDetailView, ArchiveIndexView, YearArchiveView

#entry_info_dict = (model=Entry, date_field='pub_date',)
urlpatterns = patterns('',
    # django try to match from the top
    # Examples:
    # url(r'^$', 'cms.views.home', name='home'),
    # url(r'^cms/', include('cms.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^tiny_mce/(?P<path>.*)$', 'django.views.static.server',{ 'document_root': TINYMCE_PATH}),
    #url(r'^weblog/$', ArchiveIndexView.as_view(model=Entry, date_field="pub_date"), name="entry_archive"),
    #urls for weblog
    url(r'^weblog/$', 'bruno.views.entries_index'),
    url(r'weblog/(?P<year>\d{4})/$', EntryYearArchiveView.as_view(), name="entry_year"),
    url(r'weblog/(?P<year>\d{4})/(?P<month>\w{3})/$', EntryMonthArchiveView.as_view(), name="entry_month"),
    url(r'^weblog/(?P<year>\d{4})/week/(?P<week>\d+)/$', EntryWeekArchiveView.as_view(), name="entry_week"),
    url(r'^weblog/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', DateDetailView.as_view(queryset=Entry.objects.all(), date_field='pub_date'), name="date_detail"),
    url(r'', include('django.contrib.flatpages.urls')),
)
