from django import forms
from course.models import Branch, Group, Student


class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ('name', 'address', 'photo')

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('name', 'Branch', 'photo')


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'date_of_birth', 'address', 'phone_number', 'gender', 'group', 'photo', 'courses')