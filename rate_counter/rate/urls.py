from django.conf.urls import url

from .views import (
    create_table,
    tables_list,
    table_detail,
    create_row,
    delete_row,
    delete_table,
    edit_rows,
    get_subject_from_db,
    reset_subjects,
    edit_table,
)

urlpatterns = [
    url(r'^create/$', create_table, name='create'),
    url(r'^edit_table/(?P<id>\d+)/$', edit_table, name='edit_table'),
    url(r'^delete_table/(?P<id>\d+)/$', delete_table, name='delete_table'),
    url(r'^$', tables_list, name='tables_list'),
    url(r'^detail/(?P<id>\d+)/$', table_detail, name='table_detail'),
    url(r'^create_row/(?P<id>\d+)/$', create_row, name='create_row'),
    url(r'^delete_row/(?P<id>\d+)/$', delete_row, name='delete_row'),
    url(r'^edit_rows/(?P<id>\d+)/$', edit_rows, name='edit_rows'),
    url(r'^get_subjects/(?P<id>\d+)/$', get_subject_from_db, name='get_subjects'),
    url(r'^reset_subjects/(?P<id>\d+)/$', reset_subjects, name='reset_subjects'),
]
