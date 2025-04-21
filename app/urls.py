from .views import ClassViewSet, TeacherViewSet , StudentViewSet , AdminViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register("class" , ClassViewSet)
router.register("admin" , AdminViewSet , basename='admin')
router.register("teacher" , TeacherViewSet , basename='teacher')
router.register("student" , StudentViewSet)

urlpatterns = router.urls
