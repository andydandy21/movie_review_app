from allauth.account import app_settings
from allauth.account.adapter import get_adapter
from allauth.account.models import EmailAddress
from allauth.account.utils import filter_users_by_email
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _

class CustomUserCreationForm(UserCreationForm):

    class Meta:

        model = get_user_model()
        fields = ('email', 'username',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:

        model = get_user_model()
        fields = ('email', 'username',)

class EmailChangeForm(forms.Form):

    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={"type": "email"}))

    def __init__(self, *args, **kwargs):

        self.user = kwargs.pop('user')
        super(EmailChangeForm, self).__init__(*args, **kwargs)

    def clean(self):

        self.cleaned_data['user'] = self.user
        return super().clean()

    def clean_email(self):

        value = self.cleaned_data["email"]
        value = get_adapter().clean_email(value)
        errors = {
            "this_account": _(
                "This e-mail address is already associated" " with this account."
            ),
            "different_account": _(
                "This e-mail address is already associated" " with another account."
            ),
            "max_email_addresses": _("You cannot add more than %d e-mail addresses."),
        }
        users = filter_users_by_email(value)
        on_diff_account = [u for u in users if u.pk != self.user.pk]
        primary_on_this_account = str(EmailAddress.objects.filter(user=self.user, primary=True).first())

        if primary_on_this_account == str(value):
            raise forms.ValidationError(errors["this_account"])
        if on_diff_account and app_settings.UNIQUE_EMAIL:
            raise forms.ValidationError(errors["different_account"])
        if not EmailAddress.objects.can_add_email(self.user):
            raise forms.ValidationError(
                errors["max_email_addresses"] % app_settings.MAX_EMAIL_ADDRESSES
            )
        return value

    def save(self, request):

        return EmailAddress.objects.add_email(
            request, self.user, self.cleaned_data["email"], confirm=True
        )