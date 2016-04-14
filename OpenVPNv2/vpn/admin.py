from django.contrib import admin

# Register your models here.
from .models import General,PathsVPN

class PostAdmin(admin.ModelAdmin):
    list_display = ['general_vpn_name','general_server_ip', 'general_server_port']
    list_filter = ['general_vpn_name','general_server_ip'   ]
    search_fields = ['general_vpn_name','general_server_ip' ]
    class Meta:
        model = General


admin.site.register(General, PostAdmin)
admin.site.register(PathsVPN)
