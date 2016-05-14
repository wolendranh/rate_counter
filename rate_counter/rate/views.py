import json
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, get_object_or_404, get_list_or_404, render
from django.template import RequestContext

from .forms import TableForm
from .models import Institute, Subject, StudentGroup, Table, TableRow
from .utils import get_result, get_color, rate_graphs, rate_graphs_pie
# Create your views here.


@login_required(login_url='login')
def create_table(request):
    """
    creation of new table
    """
    form = TableForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return HttpResponseRedirect(reverse('rate:table_detail', args=[instance.id]))
    context = {
        'form': form
    }
    return render(request=request, template_name="table_form.html", context=context)


def edit_table(request, id=None):
    """
    edit of existing table
    """
    table_obj = get_object_or_404(Table, id=id)
    form = TableForm(request.POST or None, request.FILES or None, instance=table_obj)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(reverse('rate:table_detail', args=[instance.id]))
    context = {
        'form': form
    }
    return render(request=request, template_name="table_form.html", context=context)


def delete_table(request, id=None):
    """
    table removal
    """
    table_obj = Table.objects.get(id=id)
    table_obj.delete()
    return HttpResponseRedirect(reverse("rate:tables_list"))


def tables_list(request):
    """
    get page with all tables
    """
    queryset = Table.objects.all()

    context = {
        "tables_list": queryset
    }

    return render(request, "tables_list.html", context)


def table_detail(request, id=None):
    """
    get page with a particular table
    """
    inst_set = Institute.objects.all()
    grp_set = StudentGroup.objects.all()
    institute = request.POST.get('Institutes')
    table_obj = get_object_or_404(Table, id=id)
    table_rows = TableRow.objects.filter(table=table_obj)
    context = {
        'color': get_color(get_result(table_rows)),
        'inst_set': inst_set,
        'grp_set': grp_set,
        'institute': institute,
        'result': get_result(table_rows),
        'table': table_obj,
        'rows': table_rows
    }
    return render(request, "table_detail.html", context)


def create_row(request, id=None):
    """
    creation of new row for particular table
    """
    table_obj = Table.objects.get(id=id)
    TableRow.objects.create(table=table_obj, name='', coefficient=1, point=0)
    return HttpResponseRedirect(reverse('rate:table_detail', args=[table_obj.id]))


def edit_rows(request, id=None):
    """
    saving changes after table rows editing
    """
    table_obj = get_object_or_404(Table, id=id)
    rows = get_list_or_404(TableRow, table=table_obj)
    for row in rows:
        row.name = request.POST.get('name{}'.format(row.id))
        row.coefficient = request.POST.get('coef{}'.format(row.id))
        row.point = request.POST.get('grade{}'.format(row.id))
        row.save()

    return HttpResponseRedirect(reverse('rate:table_detail', args=[table_obj.id]))


def delete_row(request, id=None):
    """
    particular row removal
    """
    row = TableRow.objects.get(id=id)
    table_obj = row.table
    row.delete()
    return HttpResponseRedirect(reverse('rate:table_detail', args=[table_obj.id]))


def get_subject_from_db(request, id=None):
    """
    creation of table with subject set related to group
    """
    table_obj = get_object_or_404(Table, id=id)
    grp_id = request.POST.get('Groups')
    grp_obj = get_object_or_404(StudentGroup, site_id=grp_id)
    subjects = get_list_or_404(Subject, group=grp_obj)
    for subject in subjects:
        TableRow.objects.get_or_create(table=table_obj, name=subject.name)
        # if you accidentally removed one of your row it will not overload all your table
    return HttpResponseRedirect(reverse('rate:table_detail', args=[table_obj.id]))


def reset_subjects(request, id=None):
    """
    creation of table with subject set related to group
    with deleting all of previous rows
    """
    table_obj = get_object_or_404(Table, id=id)
    old_set = get_list_or_404(TableRow, table=table_obj)
    for row in old_set:
        row.delete()
    grp_id = request.POST.get('Groups')
    grp_obj = get_object_or_404(StudentGroup, site_id=grp_id)
    subjects = get_list_or_404(Subject, group=grp_obj)
    for subject in subjects:
        TableRow.objects.get_or_create(table=table_obj, name=subject.name)
    return HttpResponseRedirect(reverse('rate:table_detail', args=[table_obj.id]))


def show_graphs_column(request, id=None):
    """
    reflects score of each subject in a column chart
    """
    context = {
        'table_data': json.dumps(rate_graphs(id)),
        'id': id,
    }
    return render(request, 'column_graphs.html', context)


def show_graphs_pie(request, id=None):
    """
    this block display pie graphs in percents of subject point
    """
    context = {
        'table_data': json.dumps(rate_graphs_pie(id)),
        'id': id,
    }
    return render(request, 'pie_graphs.html', context)


def statistics(request):
    return render(request, "statistics.html", {})
