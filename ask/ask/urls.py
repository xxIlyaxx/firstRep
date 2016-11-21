from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'qa.views.main'),
    url(r'^login\/?$', 'qa.views.test', name='login'),
    url(r'^signup\/?$', 'qa.views.test', name='signup'),
    url(r'^question\/(?P<id>\d+)\/?$', 'qa.views.question', name='question'),
    url(r'^ask\/?$', 'qa.views.ask', name='ask'),
    url(r'^popular\/?$', 'qa.views.popular', name='popular'),
    url(r'^new\/?$', 'qa.views.test', name='new'),
    url(r'^answer\/?$', 'qa.views.answer', name='answer'),
)
