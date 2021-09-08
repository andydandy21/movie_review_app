from django.conf import settings
from django.core.mail import send_mail
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView, FormView


from .forms import ContactForm


class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ContactPageView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm

    def post(self, request, *args, **kwargs):

        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            body = [
                form.cleaned_data['first_name'], 
                form.cleaned_data['last_name'], 
                form.cleaned_data['email_address'], 
                form.cleaned_data['message'], 
			]
            message = '\n'.join(body)
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])
            return redirect('contact')
        return HttpResponse('We encountered a problem. E-mail has not been sent <a href="/">return to site</a>')

    def form_valid(self, form):
        
        form.save()
        return super().form_valid(form)