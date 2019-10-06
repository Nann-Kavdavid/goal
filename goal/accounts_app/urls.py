from django.urls import path, include
from accounts_app import views
from django.contrib.auth import views as auth_views

app_name = 'accounts_app'

urlpatterns = [
    # accounts/
    path('', views.index, name='home'),
    path('signup/', views.UserSignUpView.as_view(), name='signup'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='accounts_app:home'), name='logout'),
]
