from rest_framework.routers import DefaultRouter

from .views import NewsView

router = DefaultRouter()


router.register(r'', NewsView)

urlpatterns = router.urls
