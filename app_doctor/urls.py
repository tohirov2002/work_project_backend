from rest_framework.routers import DefaultRouter

from .views import DoctorCategoryView, DoctorView

router = DefaultRouter()

router.register(r'category', DoctorCategoryView)
router.register(r'', DoctorView)

urlpatterns = router.urls
