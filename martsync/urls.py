
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf import settings
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from users.views import HomeView
from django.conf.urls.static import static


urlpatterns = [
    path("", HomeView.as_view(), name="Home"),
    path('admin/', admin.site.urls),
    # path('docs/', include_docs_urls(title="Api Documentation")),
    # path('schema/', get_schema_view(
    #     title="HRMS Backend",
    #     description="An Api build on top of django and drf that serves as a backend for a erp platform.",
    #     version='1.0.0'
    # ), name="api_schema"),
    path("auth/", include('users.urls')),
    path("api/", include("stores.urls")),
    path("api/", include("products.urls")),
    path('auth/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),



]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)