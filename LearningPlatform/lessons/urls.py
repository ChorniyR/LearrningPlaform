from django.urls import path

from .views import LessonsDetail, StepDetail, LessonsList


app_name = 'lessons'
urlpatterns = [
    path('', LessonsList.as_view()),
    path('<int:id>/', LessonsDetail.as_view()),
    path('<int:lesson_id>/step/<int:number>/', StepDetail.as_view()),
]
