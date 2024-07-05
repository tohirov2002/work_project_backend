from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import CommentView

router = DefaultRouter()
router.register(r'', CommentView, basename='comment')

urlpatterns = router.urls
