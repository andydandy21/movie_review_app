from django.urls import path

from .views import (
    ProfileDeleteView, 
    ProfileDetailView, 
    EmailChangeView, 
    LoggedInPasswordResetView, 
    ProfileDeleteView,
    ProfileReviewUpdateView,
    ProfileReviewDeleteView,
    )


urlpatterns = [
    path('profile/', ProfileDetailView.as_view(), name='user_profile'),
    path('email_change/', EmailChangeView.as_view(), name='email_change'),
    path('logged_in_password_reset', LoggedInPasswordResetView.as_view(), name='logged_in_password_reset'),
    path('post/<int:pk>/delete/', ProfileDeleteView.as_view(), name='profile_delete'),
    path('review/update/', ProfileReviewUpdateView.as_view(), name='profile_review_update'),
    path('review/delete/', ProfileReviewDeleteView.as_view(), name='profile_review_delete'),
]