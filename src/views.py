from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Team, Question, History
from . import utils
from .authentication import SingleSessionAuthentication, generate_token

import re



@api_view(['GET'])
def simple_view(request):
    MAX_QUESTIONS = Question.objects.all().count()
    return Response({"total questions": MAX_QUESTIONS}, status=status.HTTP_200_OK)

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
        
        next_question_id = team.question.id if team.question else None
                        
        return Response({
            'team_code': team.code,
            'team_name': team.name,
            'token': team.token,
            'actual_score': team.question.number - 1,
            'next_question_id': next_question_id
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
def get_question(request, id: str):
    team = request.user
    
    try:
        if team.question.id == id:
            question = Question.objects.get(id=id)
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
@permission_classes([IsAuthenticated])
@authentication_classes([SingleSessionAuthentication])
def check_answer(request, id: str):
    team = request.user
    answer = request.data.get('answer', None)
    
    if not answer:
        return Response(
            {'error': 'Answer not provided'}, 
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        if team.question.id != id:
            return Response(
                {'error': 'Team is not eligible for this question'}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        question = team.question
        result = utils.chech_with_LLM(question, answer)
        
        if result:
            
            MAX_QUESTIONS = Question.objects.all().count()
            if question.number == MAX_QUESTIONS:
                flag = utils.ontime_flag(team.code, MAX_QUESTIONS)
                score = Question.objects.get(number=MAX_QUESTIONS)

                history = History(team=team, score=score, flag=flag)
                team.question = None
                
                team.save()
                history.save()
                
                return Response({
                    'result': 'Completed',
                    'flag': flag,
                    'score': MAX_QUESTIONS,
                }, status=status.HTTP_200_OK)
            
            else:
                team.question = Question.objects.get(number=question.number+1)
                team.save()
                
                return Response({
                    'result': True,
                    'next_question_id': team.question.id
                }, status=status.HTTP_200_OK)           

        else:
            flag = utils.ontime_flag(team.code, question.number-1)
            score = Question.objects.get(number=question.number-1)

            history = History(team=team, score=score, flag=flag)
            history.save()
            
            team.question = Question.objects.get(number=1)
            team.save()
            
            return Response({
                'result': False,
                'flag': flag,
                'score': score.number,
                'next_question_id': team.question.id,
            }, status=status.HTTP_200_OK)
        
    except AttributeError:
        return Response(
            {'error': 'Team passed all questions'}, 
            status=status.HTTP_404_NOT_FOUND
        )
        
    except Exception as e:
        return Response(
            {'error': str(e)}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SingleSessionAuthentication])
def get_status(request):
    team = request.user
    
    if team.question:
        score = team.question.number - 1
    else:
        score = Question.objects.all().count()
    
    try:
        team_history = History.objects.filter(team=team).order_by('timestamp')

        return Response({
            'team_code': team.code,
            'team_name': team.name,
            'actual_score': score,
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
    
    