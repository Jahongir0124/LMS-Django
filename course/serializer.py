from rest_framework.serializers import ModelSerializer
from . models import Task


class TaskCreteSerializer(ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        
        
        return super().create(validated_data)
    

class TaskDetailSerializer(ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'