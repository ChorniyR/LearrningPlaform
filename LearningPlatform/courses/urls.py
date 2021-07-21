from django.urls import include, path
from rest_framework import routers

from .views import CoursesViewSet


router = routers.SimpleRouter()
router.register(r'', CoursesViewSet)

urlpatterns = router.urls

