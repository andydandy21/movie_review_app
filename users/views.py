from allauth.account.forms import ResetPasswordForm
from allauth.account.models import EmailAddress
from django.contrib import messages
from django.views.generic import FormView
from django.views.generic.base import TemplateView, View
from django.urls import reverse_lazy

from .forms import EmailChangeForm


class ProfileDetailView(TemplateView):

    template_name = "profile_detail.html"

class EmailChangeView(FormView):

    template_name = "profile_detail.html"
    form_class = EmailChangeForm

    def form_valid(self, form):

        user = form.cleaned_data['user']
        EmailAddress.objects.filter(user=user).exclude(primary=True).delete()
        form.save(self.request)
        messages.add_message(self.request, messages.INFO, 'E-mail confirmation has been sent to the requested address.')
        return super(EmailChangeView, self).form_valid(form)
    
    def get_success_url(self):

        return reverse_lazy('user_profile')

    def get_form_kwargs(self):
        
        kwargs = super(EmailChangeView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class LoggedInPasswordResetView(FormView):

    template_name="profile_detail.html"
    form_class = ResetPasswordForm

    def form_valid(self, form):
        form.save(self.request)
        messages.add_message(self.request, messages.INFO, 'Password reset request has been sent to your email')
        return super(LoggedInPasswordResetView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('user_profile')