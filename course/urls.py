from django.urls import path
from . views import TaskCreateView, TaskDetailView


urlpatterns = [
    path('create/', TaskCreateView.as_view()),
    path('detail/<int:id>/', TaskDetailView.as_view())
]