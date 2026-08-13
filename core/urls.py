from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

def home(request):
    return HttpResponse("""
    <h1>📝 Личный дневник</h1>
    <p>Добро пожаловать в приложение для ведения дневника!</p>
    <ul>
        <li><a href="/admin/">Админка</a></li>
        <li><a href="/swagger/">Swagger API</a></li>
        <li><a href="/api/">API</a></li>
        <li><a href="/users/login/">Войти</a></li>
    </ul>
    """)

schema_view = get_schema_view(
    openapi.Info(
        title="Diary API",
        default_version='v1',
        description="API для личного дневника",
    ),
    public=True,
)

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/', include('apps.api.urls')),
    path('users/', include('apps.users.urls')),
    path('', include('apps.diary.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger'), name='swagger'),
    path('redoc/', schema_view.with_ui('redoc'), name='redoc'),
]
