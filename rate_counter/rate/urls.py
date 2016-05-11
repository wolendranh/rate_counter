from django.conf.urls import url

import views

urlpatterns = [
    url(r'^create/$', views.create_table, name='create'),
    url(r'^edit_table/(?P<id>\d+)/$', views.edit_table, name='edit_table'),
    url(r'^delete_table/(?P<id>\d+)/$', views.delete_table, name='delete_table'),
    url(r'^$', views.tables_list, name='tables_list'),
    url(r'^(?P<id>\d+)/detail/$', views.table_detail, name='table_detail'),
    url(r'^create_row/(?P<id>\d+)/$', views.create_row, name='create_row'),
    url(r'^delete_row/(?P<id>\d+)/$', views.delete_row, name='delete_row'),
    url(r'^edit_rows/(?P<id>\d+)/$', views.edit_rows, name='edit_rows'),
    url(r'^get_subjects/(?P<id>\d+)/$', views.get_subject_from_db, name='get_subjects'),
    url(r'^reset_subjects/(?P<id>\d+)/$', views.reset_subjects, name='reset_subjects'),

    url(r'^statistics/$', views.statistics, name='statistics'),

    url(r'^graphs_column/(?P<id>\d+)/$', views.show_graphs_column, name='graphs_subject_rate'),
    url(r'^graphs_pie/(?P<id>\d+)/$', views.show_graphs_pie, name='show_graphs_pie'),

]
