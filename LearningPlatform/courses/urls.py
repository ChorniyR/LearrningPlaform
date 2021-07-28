from rest_framework import routers

from .views import CoursesViewSet

app_name = 'courses'
router = routers.SimpleRouter()
router.register(r'', CoursesViewSet)

urlpatterns = router.urls

