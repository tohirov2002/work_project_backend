from rest_framework.routers import DefaultRouter

from .views import DepartmentView

router = DefaultRouter()

router.register(r'', DepartmentView)

urlpatterns = router.urls
