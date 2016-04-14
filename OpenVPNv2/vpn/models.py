from django.db import models
#from django.conf import settings
from django.db import IntegrityError

# Create your models here.
class General(models.Model):

    class Meta:
        db_table = "general"

    general_vpn_name = models.TextField(max_length=200)
    general_project_name = models.TextField(max_length=200)
    general_server_ip = models.GenericIPAddressField()
    general_server_port = models.IntegerField()
    general_project_status = models.TextField(max_length=20)

    def __unicode__(self):
        return unicode(self.general_server_port)


class PathsVPN(models.Model):
    class Meta:
        db_table = "pathsvpn"

    pathsvpn_vpn_path = models.TextField(max_length=200)
    pathsvpn_general = models.ForeignKey(General)

    def __unicode__(self):
        return self.pathsvpn_vpn_path

class Certs(models.Model):
    class Meta():
        db_table = 'certs'
    certs_user_name = models.TextField(max_length=200)
    certs_general = models.ForeignKey(General)
#, null=True, blank=True,default=None)
class Revoke(models.Model):
    class Meta():
        db_table = 'revoke'
    certs_revoke_name = models.TextField(max_length=200)
    certs_revoke_status = models.TextField(max_length=200)
    certs_general = models.ForeignKey(General)
