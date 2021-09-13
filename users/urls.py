from django.urls import path

from .views import ProfileDetailView, EmailChangeView


urlpatterns = [
    path('profile/', ProfileDetailView.as_view(), name='user_profile'),
    path('email_change/', EmailChangeView.as_view(), name='email_change')
]