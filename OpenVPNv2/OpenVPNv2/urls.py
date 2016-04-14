from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


import vpn.views
urlpatterns = [
    # Examples:
    # url(r'^$', 'OpenVPNv2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^vpn/', include('vpn.urls')),
    url(r'^auth/', include('login.urls')),
    url(r'^', include('vpn.urls')),
]
