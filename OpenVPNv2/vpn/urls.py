from django.conf.urls import patterns, include, url

import vpn.views
urlpatterns = [
     url(r'^status_vpn/', vpn.views.status_vpn, name='status_vpn'),
     url(r'^home/$', vpn.views.home_page),
     url(r'^list_vpn/$', vpn.views.list_vpn, name="list_vpn" ),
     url(r'^manage_cert/vpn/(?P<vpn_id>\d+)', vpn.views.tabs, name="tabs"),
]

