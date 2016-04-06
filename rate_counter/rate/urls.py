from django.conf.urls import url

from .views import (
    create_table
)

urlpatterns = [
    url(r'^table/$', create_table, name='table'),

]
