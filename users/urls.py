from django.urls import path

from .views import ProfileDetailView, EmailChangeView, LoggedInPasswordResetView


urlpatterns = [
    path('profile/', ProfileDetailView.as_view(), name='user_profile'),
    path('email_change/', EmailChangeView.as_view(), name='email_change'),
    path('logged_in_password_reset', LoggedInPasswordResetView.as_view(), name='logged_in_password_reset'),
]