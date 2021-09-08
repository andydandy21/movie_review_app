from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.base import TemplateView

from .models import CustomUser


class ProfileDetailView(TemplateView):

    model = CustomUser
    template_name = "profile_detail.html"
    
    def get_context_data(self, **kwargs): 
        context = {}

        context['profile'] = self.request.user

        return context
    