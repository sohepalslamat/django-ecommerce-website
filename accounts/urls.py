from django.urls import path
from django.contrib.auth import views as auth_views

from .views import signup, activate_email

urlpatterns = [
    path('signup/', signup, name="signup"),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('activate/<int:uid>/<token>/', activate_email, name="activate_email"),
    path('password_reset/', auth_views.PasswordResetView.as_view(),
         name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name="password_reset_done"),
    path('password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),
    path('password-reset/completee/', auth_views.PasswordResetCompleteView.as_view(),
         name="password_reset_complete"),

]
