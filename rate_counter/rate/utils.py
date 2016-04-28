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
