from django.contrib import admin
from .models import Group, GroupMemeber

# Register your models here.
admin.site.register(Group)

class GroupMemberInline(admin.TabularInline):
    model = GroupMemeber