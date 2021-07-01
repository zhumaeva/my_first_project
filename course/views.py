from django.core.exceptions import AppRegistryNotReady
#from course.serializers import BranchSerializer, GroupSerializer, StudentSerializer
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, request
from rest_framework import serializers
from course.forms import GroupForm, StudentForm, BranchForm
from django.http import HttpResponse
from .models import Branch
from .models import Student
from .models import Group, Course
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def my_main_page(request):
    return render(request, 'course/my_page.html')

def branches_list(request):
    branches = Branch.objects.all()
    my_context = {'branches': branches}
    return render(request, 'course/branches_list.html', my_context)

class BranchListView(ListView):
    model = Branch
    template_name = 'course/branches_list.html'
    context_object_name = 'branches'

def branch_edit(request, branch_id):
    branch = get_object_or_404(Branch, pk=branch_id)
    if request.method == "POST":
        form = BranchForm(request.POST, request.FILES, instance=branch)
        if form.is_valid():
            branch = form.save()
            return redirect('branch_detail', branch_id=branch.id)
    else:
        form = BranchForm(instance=branch)

    return render(request, 'course/branch_create.html', {'form': form})

class BranchUpdateView(LoginRequiredMixin, UpdateView):
    model = Branch
    fields = ['name', 'address', 'photo']
    template_name = 'course/branch_edit.html'
    pk_url_kwarg = 'branch_id'
    login_url = '/user/login/'

def branch_random(request):
    branches = Branch.objects.all()
    random_branch = random.choice(branches)
    my_context = {'branch': random_branch}
    return render(request, 'course/branch_detail.html', context=my_context)


@login_required
def branch_create(request):
    if request.method == "POST":
        form = BranchForm(request.POST, request.FILES)
        if form.is_valid():
            branch = form.save()
            return redirect('branch_detail', branch_id=branch.id)
    else:
        form = BranchForm()

    return render(request, 'course/branch_create.html', {'form': form})



class BranchCreateView(CreateView):
    model = Branch
    fields = ['name', 'address', 'photo']
    template_name = 'course/branch_create.html'
    
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


def branch_detail(request, branch_id):
    branch = get_object_or_404(Branch, pk=branch_id)
    groups = Group.objects.filter(Branch=branch)
    context = {'branch': branch, 'groups': groups}
    return render(request, 'course/branch_detail.html', context=context)

class BranchDetailView(DetailView):
    model = Branch
    template_name = 'course/branch_detail.html'
    context_object_name = 'branch'
    pk_url_kwarg = 'branch_id'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = Group.objects.filter(Branch=self.object)
        return context




def branch_delete(request, branch_id):
    query = Branch.objects.get(pk=branch_id)
    query.delete()
    return HttpResponseRedirect("/course/branches/")


class BranchDeleteView(LoginRequiredMixin,DeleteView):
    model = Branch
    pk_url_kwarg = 'branch_id'
    success_url = reverse_lazy('branches_list')
    login_url = '/user/login/'


def group_list(request):
    groups = Group.objects.all()
    my_context = {'groups': groups}
    return render(request, 'course/group_list.html', context=my_context)


class GroupListView(ListView):
    model = Group
    template_name = 'course/group_list.html'
    context_object_name = 'groups'



def group_detail(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    students = Student.objects.filter(group=group)
    context = {'group': group, 'students': students}
    return render(request, 'course/group_detail.html', context=context)



class GroupDetailView(DetailView):
    model = Group
    template_name = 'course/group_detail.html'
    context_object_name = 'group'
    pk_url_kwarg = 'group_id'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student'] = Student.objects.filter(group=self.object)
        return context



def group_create(request):
    if request.method == "POST":
        form = GroupForm(request.POST, request.FILES)
        if form.is_valid():
            group = form.save()
            return redirect('group_detail', group_id=group.id)
    else:
        form = GroupForm()

    return render(request, 'course/group_create.html', {'form': form})


class GroupCreateView(CreateView):
    model = Group
    fields = ['name', 'Branch', 'photo']
    template_name = 'course/group_create.html'


def group_edit(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    if request.method == "POST":
        form = GroupForm(request.POST, request.FILES, instance=group)
        if form.is_valid():
            group = form.save()
            return redirect('group_detail', group_id=group.id)
    else:
        form = GroupForm(instance=group)

    return render(request, 'course/group_create.html', {'form': form})



class GroupUpdateView(UpdateView):
    model = Group
    fields = ['name', 'Branch', 'photo']
    template_name = 'course/group_edit.html'
    pk_url_kwarg = 'group_id'

def group_random(request):
    group = Group.objects.all()
    random_group = random.choice(group)
    my_context = {'group': random_group}
    return render(request, 'course/group_detail.html', context=my_context)

def group_delete(request, group_id):
    query = Group.objects.get(pk=group_id)
    query.delete()
    return HttpResponseRedirect("/course/groups/")


class GroupDeleteView(LoginRequiredMixin,DeleteView):
    model = Group
    pk_url_kwarg = 'group_id'
    success_url = reverse_lazy('group_list')
    login_url = '/user/login/'


def student_list(request):
    students = Student.objects.all()
    my_context = {'students': students}
    return render(request, 'course/student_list.html', context=my_context)


class StudentListView(ListView):
    model = Student
    template_name = 'course/student_list.html'
    context_object_name = 'students'


def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    my_context = {'student': student}
    return render(request, 'course/student_detail.html', context=my_context)


class StudentDetailView(DetailView):
    model = Student
    template_name = 'course/student_detail.html'
    context_object_name = 'student'
    pk_url_kwarg = 'student_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(student=self.object)
        return context

def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save()
            return redirect('student_detail', student_id=student.id)
    else:
        form = StudentForm()

    return render(request, 'course/student_create.html', {'form': form})


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    fields = ['name', 'date_of_birth', 'address', 'phone_number', 'gender', 'group', 'photo', 'courses']
    template_name = 'course/student_create.html'
    login_url = '/user/login/'


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())





def student_edit(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            student = form.save()
            return redirect('student_detail', student_id=student.id)
    else:
        form = StudentForm(instance=student)

    return render(request, 'course/student_create.html', {'form': form})


class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name', 'date_of_birth', 'address', 'phone_number', 'gender', 'group', 'photo', 'courses']
    template_name = 'course/student_edit.html'
    pk_url_kwarg = 'student_id'

def student_delete(request, student_id):
    query = Student.objects.get(pk=student_id)
    query.delete()
    return HttpResponseRedirect("/course/students/")


def student_random(request):
    students = Student.objects.all()
    random_student = random.choice(students)
    courses = random_student.courses.all
    my_context = {'student': random_student, 'courses': courses}
    return render(request, 'course/student_detail.html', context=my_context)

class StudentDeleteView(LoginRequiredMixin,DeleteView):
    model = Student
    pk_url_kwarg = 'student_id'
    success_url = reverse_lazy('student_list')
    login_url = '/user/login/'





