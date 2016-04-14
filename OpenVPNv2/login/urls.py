from django.conf.urls import patterns, include, url

import login.views
urlpatterns = [
     url(r'^login/', login.views.login, name="login"),
     url(r'^logout/', login.views.logout, name="logout"),
]