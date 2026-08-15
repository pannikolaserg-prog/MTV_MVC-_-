from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .models import User
from .forms import UserRegistrationForm

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True

class UserLogoutView(LogoutView):
    next_page = 'users:login'

class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
