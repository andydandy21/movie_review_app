import uuid
from allauth.account.models import EmailAddress
from allauth.account.signals import email_confirmed
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    
    email = models.EmailField(_('email address'))
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    @receiver(email_confirmed)
    def update_user_email(sender, request, email_address, **kwargs):

        email_address.set_as_primary()
        EmailAddress.objects.filter(user=email_address.user).exclude(primary=True).delete()