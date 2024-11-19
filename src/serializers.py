from .models import Team, Question, History
from rest_framework import serializers

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        
        
class TeamSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Team
        fields = '__all__'
        
        
class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'