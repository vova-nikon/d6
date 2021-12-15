from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from p_library.views import RegisterView, CreateReaderProfile
from allauth.account.views import login, logout

app_name = 'p_library'
urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('github_login/', login, name='github_login'),
    path('github_logout/', logout, name='github_logout'),
    path('register/', RegisterView.as_view(template_name='register.html', success_url='create_reader/'), name='register'),
    path('register/create_reader/', CreateReaderProfile.as_view(), name='create_reader'),
    
]