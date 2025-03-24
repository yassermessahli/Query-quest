from django.urls import path
from . import views

urlpatterns = [
    path('', views.simple_view, name="get_total_questions"),
    path('login/', views.login, name="do_login"),
    path('question/<str:id>/', views.get_question, name="get_question"),
    path('question/<str:id>/check/', views.check_answer, name="check_answer"),
    path('status/', views.get_status, name="get_status"),
]