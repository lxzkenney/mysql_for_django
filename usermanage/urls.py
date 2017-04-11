from django.conf.urls import patterns, include, url
from django.contrib import admin
import web.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'usermanage.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    
    #url(r'^admin/',include('app01.urls')),
    #url(r'^web/',include('web.urls')),
    url(r'^admin/',include(web.urls)),
    #url(r'^login/',AccountView.Login ),
)