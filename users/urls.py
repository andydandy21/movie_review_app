from django.urls import path

from .views import ProfileDetailView


urlpatterns = [
    path('<uuid:pk>/', ProfileDetailView.as_view(), name='user_profile'),
]