from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# drf simple jwt import
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# drf yasig import
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/department/", include('app_department.urls')),
    path("api/doctor/", include('app_doctor.urls')),
    path("api/comments/", include('app_comments.urls')),
    path("api/news/", include('app_news.urls')),
    # drf simple jwt urls
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # drf yasg urls
   # path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)