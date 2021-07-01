from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from .models import Branch, Group, Student, Course

# Register your models here

class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name', 'address')
    list_filter = ('creator', 'manager')
    raw_id_fields = ('creator', )

admin.site.register(Branch,BranchAdmin)

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'Branch')
    search_fields = ('name', 'id')
    list_filter = ('creator',)
    raw_id_fields = ('creator', )

admin.site.register(Group,GroupAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name', 'date_of_birth', 'address', 'phone_number', 'gender', 'group','courses')
    list_filter = ('creator', )
    raw_id_fields = ('creator',     )

admin.site.register(Student, StudentAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
admin.site.register(Course, CourseAdmin)