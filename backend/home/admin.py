"""
from django.contrib import admin
from django.contrib.auth.models import User
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class UserResource(resources.ModelResource):

    class Meta:
        model = User
        fields = ('id', 'username', 'password',)



class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResource
    list_display = ('id','username','password','is_staff')
    list_filter = ('is_staff', 'is_superuser')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
"""
# Register your models here.
