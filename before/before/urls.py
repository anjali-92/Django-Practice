from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'before.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/',include('users.urls')),
    url(r'^tictactoe/',include('tictactoe.urls')),
    url(r'^$','main.views.home', name='boardgames_home'),
)

urlpatterns += patterns('django.contrib.auth.views',
	url(r'^login/$','login',{'template_name':'login.html'},name='boardgames_login'),
	url(r'^logout/$','logout',{'next_page':'boardgames_home'},name='boardgames_logout'),
	)
