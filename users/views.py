from allauth.account.forms import ResetPasswordForm
from allauth.account.models import EmailAddress
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import FormView, TemplateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone

from .forms import EmailChangeForm
from .models import CustomUser
from movies.models import Review


class ProfileDetailView(LoginRequiredMixin, TemplateView):

    template_name = "profile_detail.html"

class EmailChangeView(LoginRequiredMixin, FormView):

    template_name = "profile_detail.html"
    form_class = EmailChangeForm

    def form_valid(self, form):

        user = form.cleaned_data['user']
        EmailAddress.objects.filter(user=user).exclude(primary=True).delete()
        form.save(self.request)
        messages.success(self.request, 'E-mail confirmation has been sent to the requested address.', extra_tags='confirmation_sent')
        return super(EmailChangeView, self).form_valid(form)
    
    def get_success_url(self):

        return reverse_lazy('user_profile')

    def get_form_kwargs(self):
        
        kwargs = super(EmailChangeView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class LoggedInPasswordResetView(LoginRequiredMixin, FormView):

    template_name="profile_detail.html"
    form_class = ResetPasswordForm

    def form_valid(self, form):
        form.save(self.request)
        messages.success(self.request, 'Password reset request has been sent to your email', extra_tags='confirmation_sent')
        return super(LoggedInPasswordResetView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('user_profile')

class ProfileDeleteView(LoginRequiredMixin, DeleteView):

    model = CustomUser
    success_url = reverse_lazy('home')
    
class ProfileReviewUpdateView(LoginRequiredMixin, TemplateView):

    def post(self, request, *args, **kwargs):

        review = Review.objects.get(id=request.POST['review_id'])
        review.title = request.POST['title']
        review.viewer_rating = request.POST['viewer_rating'] if 'viewer_rating' in request.POST else 0
        review.comment = request.POST['comment']
        review.date_posted = timezone.now()
        review.save()
        return redirect(reverse_lazy('user_profile'))

class ProfileReviewDeleteView(LoginRequiredMixin, TemplateView):

    def post(self, request, *args, **kwargs):

        review = Review.objects.get(id=request.POST['review_id'])
        review.delete()

        return redirect(reverse_lazy('user_profile'))