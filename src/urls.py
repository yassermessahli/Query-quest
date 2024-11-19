from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.simple_view, name="get_total_questions"),
    path('login/', views.login, name="do_login"),
    path('question/<str:id>/', views.get_question, name="get_question"),
    path('question/<str:id>/check/', views.check_answer, name="check_answer"),
    path('status/', views.get_status, name="get_status"),
]

class_based_views_urlpatterns = [
    path('team/', views.TeamGenericView.as_view(), name='team-list-create'),
    path('team/<str:code>/', views.TeamGenericView.as_view(), name='team-detail-update-delete'),
    
    path('question/', views.QuestionGenericView.as_view(), name='question-list-create'),
    path('question/<int:number>/', views.QuestionGenericView.as_view(), name='question-detail-update-delete'),
    
    path('history/', views.HistoryGenericView.as_view(), name='history-list-create'),
    path('history/<str:team>/<int:score>/', views.HistoryGenericView.as_view(), name='history-detail-update-delete'),
]

urlpatterns += class_based_views_urlpatterns