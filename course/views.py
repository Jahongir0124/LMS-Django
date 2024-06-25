from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from . serializer import TaskCreteSerializer, TaskDetailSerializer
from rest_framework.response import Response
from acconts.serializer import CourseSerializer

#Create Task by Teacher
class TaskCreateView(ListCreateAPIView):
    
    queryset = Task.objects.all()
    serializer_class = TaskCreteSerializer
    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):

        serializer = TaskCreteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)
    
#Task-detail View
class TaskDetailView(ListAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer

    def get(self, request, id):
        tasks = Task.objects.filter(course_id=id)
        serializer = self.serializer_class(tasks, many=True)

        return Response(serializer.data)
