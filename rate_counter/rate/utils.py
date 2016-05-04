from django.shortcuts import get_list_or_404
from .models import TableRow
#
# I am not sure, but I think all of this imports are redundant
#
# import os
# import subprocess
# from django.core.wsgi import get_wsgi_application
# os.environ['DJANGO_SETTINGS_MODULE'] = 'rate_counter.settings'
# application = get_wsgi_application()


def get_color(result):
    if result < 71:
        color = 'danger'
    elif 71 <= result < 88:
        color = 'warning'
    else:
        color = 'success'
    return color


def get_result(table_rows):
    coef_sum, point_sum, result = 0, 0, 0
    if table_rows:
        for row in table_rows:
            coef_sum += row.coefficient
            point_sum += (row.point * row.coefficient)
        if point_sum:
            result = point_sum / coef_sum
    return round(result, 2)


def rate_graphs(id):
    """
    prepare data for json column charts
    """
    table_rows = get_list_or_404(TableRow, table_id=id)
    table_data = [['Rate Graphs'], ['100']]
    for row in table_rows:
        table_data[0].append(row.name)
        table_data[1].append(row.point)
    return table_data


def rate_graphs_pie(id):
    """
    prepare data for json pie charts
    """
    table_rows = get_list_or_404(TableRow, table_id=id)
    table_data = [['Rate', 'Subject']]
    for row in table_rows:
        table_data.append([row.name, row.point])
    return table_data
