from django.conf.urls import patterns, include, url
import os
SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = os.path.dirname(SETTINGS_DIR)
TINYMCE_PATH = PROJECT_PATH + "/tinymce/js/tinymce"


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

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
    url(r'', include('django.contrib.flatpages.urls')),
)
