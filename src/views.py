from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Team, Question, History
from . import utils
from .authentication import SingleSessionAuthentication, generate_token

import re



@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello, World!"}, status=status.HTTP_200_OK)

@api_view(['POST'])
def login(request):
    team_code = request.data.get('team_code', None)
    
    if not team_code or not re.match(r'^\d{8}$', team_code):
        return Response(
            {'error': 'Invalid team code format'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
        
    try:
        team = Team.objects.get(code=team_code)
        token = generate_token()
        team.token = token
        team.save()
        
        return Response({
            'team_code': team.code,
            'team_name': team.name,
            'token': team.token,
            'actual_score': team.question.number
            },
            status=status.HTTP_200_OK
        )
        
    except Team.DoesNotExist:
        return Response(
            {'error': 'Team not registered'}, 
            status=status.HTTP_404_NOT_FOUND
        )

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SingleSessionAuthentication])
def get_question(request, id):
    team = request.user
    
    try:
        question = Question.objects.get(number=id)
        
        if team.question.number == question.number:
            return Response({
                'id': question.id,
                'number': question.number,
                'durations': question.duration,
                'statement': question.statement,
                'task': question.task,
                'exp_output': question.exp_output,
                'typical_answer': question.typical_answer,
            }, status=status.HTTP_200_OK)
        else:
            return Response(
                {'error': 'Team is not eligible for this question'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
    except Question.DoesNotExist:
        return Response(
            {'error': 'Question not found'}, 
            status=status.HTTP_404_NOT_FOUND
        )

@api_view(['POST'])
def check_answer(request, id):
    raise NotImplementedError

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SingleSessionAuthentication])
def get_status(request):
    team = request.user
    
    try:
        team_history = History.objects.filter(team=team).order_by('timestamp')

        return Response({
            'team_code': team.code,
            'team_name': team.name,
            'actual_score': team.question.number,
            'history': [
                {
                    'timestamp': history.timestamp,
                    'reached_score': history.score.number,
                    'flag': history.flag
                }
                for history in team_history
            ]
        }, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response(
            {'error': str(e)}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    
    