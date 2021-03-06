from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm


CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):

    add_form = CustomUserCreationForm
    add_fieldsets = (
        (None, {
            'fields': ('email','username','password1','password2'),
        }),
    )
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]

admin.site.register(CustomUser, CustomUserAdmin)