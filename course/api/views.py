import re
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from course.api.serializers import *
from course.models import Branch, Student, Group
from rest_framework import generics, mixins


# class BranchListView(generics.ListCreateAPIView):
#     queryset = Branch.objects.all()
#     serializer_class = BranchModelSerializer
#
#
# class BranchDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Branch.objects.all()
#     serializer_class = BranchModelSerializer


class BranchListView(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    generics.GenericAPIView):

    queryset = Branch.objects.all()
    serializer_class = BranchModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post( self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BranchDetailView(mixins.DestroyModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.RetrieveModelMixin,
                       generics.GenericAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchModelSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class BranchAPIView(APIView):

    def get(self, request, format=None):
        branches = Branch(Serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = BranchModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class GroupListView(generics.ListCreateAPIView):
#     queryset = Group.objects.all()
#     serializer_class = GroupModelSerializer
#
#
# class GroupDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Group.objects.all()
#     serializer_class = GroupModelSerializer

class GroupListView(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    generics.GenericAPIView):

    queryset = Group.objects.all()
    serializer_class = GroupModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post( self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class GroupDetailView(mixins.DestroyModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.RetrieveModelMixin,
                       generics.GenericAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupModelSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class GroupAPIView(APIView):

    def get(self, request, format=None):
        groups = Group.objects.all()
        serializer = GroupModelSerializer(groups, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = GroupModelSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class StudentListView(generics.ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentModelSerializer
#
#
# class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentModelSerializer


class StudentListView(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    generics.GenericAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post( self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StudentDetailView(mixins.DestroyModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.RetrieveModelMixin,
                       generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class StudentAPIView(APIView):
    def get(self, request, format=None):
        students = Student.objects.all()
        serializer = StudentModelSerializer(students, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = StudentModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
class BranchDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            branch = Branch.objects.get(pk=pk)
            return branch
        except Branch.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        branch = self.get_object(pk)
        serializer = BranchModelSerializer(branch)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        branch = self.get_object(pk)
        serializer = BranchModelSerializer(instance=branch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        branch = self.get_object(pk)
        branch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GroupDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            group = Group.objects.get(pk=pk)
            return group
        except Group.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        group = self.get_object(pk)
        serializer = GroupSerializer(group)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        group = self.get_object(pk)
        serializer = GroupSerializer(instance=group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        group = self.get_object(pk)
        group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StudentDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            student = Student.objects.get(pk=pk)
            return student
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentSerializer(instance=student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        student = self.get_object(pk)
        student.delete()