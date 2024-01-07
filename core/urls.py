from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/v1/', include('blog.urls')),
    path('api/v1/auth/', include('authentication.urls')),
    path('api/v1/education/', include('education.urls')),
    path('api/v1/university/', include('University.urls')),
    path('api/v1/profile/', include('Profile.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

if settings.DEBUG:


    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
