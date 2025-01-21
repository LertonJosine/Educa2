from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth import get_user_model


class CustomAdmin(UserAdmin):
    model = get_user_model()
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = [
        'username', 
        'email',
        'is_superuser'
    ]
    
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", 'user_permissions', 'groups'),
            },
        ),
    )
    
admin.site.register(get_user_model(), CustomAdmin)