from django.urls import path

from .views import LessonsDetail, StepDetail

urlpatterns = [
    path('<int:id>/', LessonsDetail.as_view()),
    path('<int:lesson_id>/step/<int:id>/', StepDetail.as_view()),
]
