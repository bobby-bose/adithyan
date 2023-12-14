from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.http import JsonResponse, HttpResponse
import json

schema_view = get_schema_view(
    openapi.Info(
        title='API',
        default_version='v1',
        description='Test',
    ),
    public=False,
    permission_classes=[permissions.AllowAny],
)

def swagger_json(request):
    try:
        schema = schema_view().schema
        return JsonResponse(schema, safe=False)  # Set safe parameter to False
    except Exception as e:
        error_message = {'error': str(e)}
        return JsonResponse(error_message, status=500)

def download_swagger_json(request):
    try:
        schema = schema_view().schema
        swagger_json = json.dumps(schema, indent=2)
        response = HttpResponse(swagger_json, content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="swagger.json"'
        return response
    except Exception as e:
        error_message = {'error': str(e)}
        return JsonResponse(error_message, status=500)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger'),
    path('api/v1/', include('blog.urls')),
    path('api/v1/auth/', include('authentication.urls')),
    path('api/v1/education/', include('education.urls')),
    path('download/swagger.json/', download_swagger_json, name='download-swagger-json'),
]

if settings.DEBUG:


    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
