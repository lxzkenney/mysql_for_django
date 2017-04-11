from django.conf.urls import patterns, include, url
from django.contrib import admin
from web import views
from web.views import HomeView,AccountView
from web.views import db
from web.views import runcmd

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'usermanage.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^login/',AccountView.Login ),
    url(r'^index/',HomeView.Index),
    #url(r'^userlist/(?P<id>\d*)',HomeView.UserList),
    url(r'^userlist/$',HomeView.UserList),
    url(r'^userdetail/(?P<id>\d*)/$',HomeView.UserDetail),
    url(r'^adduser/',HomeView.AddUser),
    url(r'^deluser/',HomeView.DelUser),
    url(r'^loginform/',AccountView.LoginByForm ),
    url(r'^install/',db.install),
    url(r'^manage/',db.manage),
    url(r'^web/',db.manage),
    url(r'^iplist/',db.Model),
    url(r'^backup/',db.backup),
    url(r'^autobackup/',db.autobackup),
    url(r'^runcmd/',runcmd.cmdindex),
    url(r'^cmdresult/',runcmd.cmdresult),
)
