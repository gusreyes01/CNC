from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CNC.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'app.views.home', name='home'),
    url(r'^horizontal/$', 'app.views.horizontal', name='horizontal'),
    url(r'^vertical/$', 'app.views.vertical', name='vertical'),
    url(r'^vertical/V1/$', 'app.views.vertical_V1', name='vertical_V1'),

)

# Add the static files pattern to the url.
urlpatterns += staticfiles_urlpatterns()
