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
    url(r'^vertical/V2/$', 'app.views.vertical_V2', name='vertical_V2'),
    url(r'^vertical/V3/$', 'app.views.vertical_V3', name='vertical_V3'),
    url(r'^vertical/V4/$', 'app.views.vertical_V4', name='vertical_V4'),
    url(r'^horizontal/H1/$', 'app.views.horizontal_V1', name='horizontal_V1'),
    url(r'^horizontal/H2/$', 'app.views.horizontal_V2', name='horizontal_V2'),
    url(r'^horizontal/H3/$', 'app.views.horizontal_V3', name='horizontal_V3'),
    url(r'^horizontal/H4/$', 'app.views.horizontal_V4', name='horizontal_V4'),

)

# Add the static files pattern to the url.
urlpatterns += staticfiles_urlpatterns()
