from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):
    site_title = 'Pulse'
    site_header = 'Pulse'
    index_title = 'Pulse'

admin_site = MyAdminSite()