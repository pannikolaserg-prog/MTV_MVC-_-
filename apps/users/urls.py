from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import UserRegistrationView

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/users/login/'), name='logout'),
    path('register/', UserRegistrationView.as_view(), name='register'),
]
