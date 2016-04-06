from django.shortcuts import render
from .models import Institute, Subject, StudentGroup

# Create your views here.


def create_table(request):

    inst_set = Institute.objects.all()
    grp_set = StudentGroup.objects.all()
    subj_set = Subject.objects.all()
    institute = request.POST.get('Institutes')
    group = request.POST.get('Groups')

    context = {
        'inst_set': inst_set,
        'grp_set': grp_set,
        'subj_set': subj_set,
        'institute': institute,
        'group': group,
    }
    return render(request=request, template_name="table.html", context=context)
