from django.http.response import  HttpResponse, Http404, HttpResponseRedirect
from django.template.loader import get_template
from django.shortcuts import render_to_response, redirect
from vpn.models import General, Revoke, PathsVPN
from forms import GenerateCertUsr, RevokeCertUsr
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_protect
from vpn.services import generate_certs,revoke_certs, stats_certs
import subprocess
from django.contrib import auth


# Create your views here.

def status_vpn(request):

    list_ports = []
    for port in General.objects.all ():
        list_ports.append(port)
        get_status = subprocess.check_output(
            'netstat -nlp | grep {0}; exit 0'.format(port),
            stderr=subprocess.STDOUT, shell=True)
        if str(port) in str(get_status):
            General.objects.filter(
                general_server_port='{0}'.format(port))\
                .update(general_project_status='Running')
        else:
            General.objects.filter(general_server_port='{0}'.format(port))\
                .update(general_project_status='Stoped')

    return render_to_response('status_vpn.html',
                              {'general': General.objects.all()})

def home_page(request):
    return render_to_response('index.html', {'username': auth.get_user(request).username} )

@csrf_protect
def tabs(request,vpn_id=1):
    path = PathsVPN.objects.get(pathsvpn_general_id=vpn_id)
    name_vpn = General.objects.get(id=vpn_id)
    form = RevokeCertUsr()
    gform = GenerateCertUsr(initial={'location_certificate' : '/etc/openvpn/',
                                     'send_email_certificate': 'oleh.hrebchuk@eleks.com'})
    print request.POST
    if request.method == 'POST':
        gform = GenerateCertUsr(request.POST)
        form = RevokeCertUsr(request.POST)
        if gform.is_valid():
            data = gform.cleaned_data
            print data
            generate_certs(data,path)
        elif form.is_valid():
            data = form.cleaned_data
            revoke_certs(data,path)
            revoke_certs(data,path)
    if request.POST.get('Refresh') == 'Refresh':
                print 'true'
                stats_certs(path,vpn_id)
    context = {
		"form": form,
        "gform": gform,
        "sform": Revoke.objects.filter(certs_general_id=vpn_id),
        "name_vpn": name_vpn,
	}
    return TemplateResponse(request, 'user_managment_cert.html', context)

def list_vpn(request, vpn_id=1):
    args = {}
    args['form'] = General.objects.all()
    return render_to_response('list_vpns.html',args)



