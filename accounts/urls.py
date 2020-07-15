from django.urls import path
from django.contrib.auth import views as auth_views

from .views import signup, activate_email

urlpatterns = [
    path('signup', signup, name="signup"),
    path('login', auth_views.LoginView.as_view(), name="login"),
    path('logout', auth_views.LogoutView.as_view(), name="logout"),
    path('activate/<int:uid>/<token>/', activate_email, name="activate_email"),

]
