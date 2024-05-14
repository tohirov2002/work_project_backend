from rest_framework.routers import DefaultRouter

from .views import DepartmentCategoryView, DepartmentView

router = DefaultRouter()

router.register(r'category', DepartmentCategoryView)
router.register(r'', DepartmentView)

urlpatterns = router.urls
