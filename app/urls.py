from .views import ClassViewSet, TeacherViewSet , StudentViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register("class" , ClassViewSet)
router.register("teacher" , TeacherViewSet , basename='teacher')
router.register("student" , StudentViewSet)

urlpatterns = router.urls