from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from . serializer import LoginSerializer, UserSerializer, CourseSerializer
from django.contrib.auth import authenticate
from . models import User, Teacher, Student
from groups.models import Group
from course.models import Course
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.shortcuts import get_object_or_404



#Login View use JWT token
class LoginAPIView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data["password"]
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'teacher': user.is_teacher,
                'student': user.is_student,
                'is_staff': user.is_staff,
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response("sdsd", status=status.HTTP_400_BAD_REQUEST)

#Profil-Student View
class ProfileStudent(APIView):
    

    def get(self, request):

        user = request.user
        student = Student.objects.get(user=user)
        try:
            group = Group.objects.get(student=student)
        except Exception as e:
            group = None
        courses = Course.objects.filter(group=group)
        serializer = CourseSerializer(courses, many=True)
        data = {
            'id': student.id,
            'fullName': student.first_name + " " + student.last_name,
            'group': group.number_group,
            'courses': serializer.data
        }

        return Response(data)
   
    
#Profil-Teacher view
class ProfileTeacher(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        teacher = Teacher.objects.get(user=request.user)
        course = Course.objects.filter(teacher=teacher)
        serialzer = CourseSerializer(course, many=True)
        
        data = {
            'fullName': teacher.first_name + " " + teacher.last_name,
            'degree': teacher.degree,
            'course': serialzer.data
        }

        return Response(data)
    

class AdminView(APIView):

    permission_classes = [IsAdminUser]

    def get(self, request):
        
        pass

    def post(self, request):
        pass