from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.diary.urls')),
    path('users/', include('apps.users.urls')),  # Добавляем users
    path('api/', include('apps.api.urls')),
]

# Добавляем стандартные URL для авторизации (опционально)
from django.contrib.auth import views as auth_views
urlpatterns += [
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]
