from django.urls import path
from .views import LoginAPIView, ProfileStudent, ProfileTeacher

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('dashboard-student/', ProfileStudent.as_view()),
    path('dashboard-teacher/', ProfileTeacher.as_view())
]