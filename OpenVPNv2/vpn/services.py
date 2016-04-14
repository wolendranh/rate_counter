import pexpect
import os
from vpn.models import Revoke
from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'OpenVPNv2.settings'
application = get_wsgi_application()


def generate_certs(data,path):
    """

    :type data: object
    """
    print data.items()
    os.chdir('{0}easy-rsa/'.format(path))
    child = pexpect.spawn('/bin/bash')
    child.sendline('source ./vars')
    child.sendline('./build-key {0}'.format(data['name_certificate']))
    for i in range(10):
        child.sendline('')
    child.sendline('y')
    child.sendline('y')

def revoke_certs(data,path):
    """
    in this case we revoke users openvpn certificates
    :type data: object
    """
    print dict(data.items())
    os.chdir('{0}easy-rsa/'.format(path))
    child = pexpect.spawn('/bin/bash')
    child.sendline('source ./vars')
    child.sendline('./revoke-full {0}'.format(data['name_certificate']))
    child.sendline('\n')

def stats_certs(path,vpn_id):
    dir_vpn = '{0}easy-rsa/keys/index.txt'.format(path)
    file = open(dir_vpn, 'r')
    name=''
    all_entry = Revoke.objects.filter(certs_revoke_name='{}'.format(name))
    for line in file:
        status = line[0]
        start = line.index('/CN=') + len('/CN=')
        end = line.index('/name=')
        slise = line[start:end]
        if  Revoke.objects.filter(certs_revoke_name='{0}'.format(slise)):
            pass
        else:
            b = Revoke(certs_revoke_name=slise,certs_revoke_status=status,certs_general_id=vpn_id)
            b.save()