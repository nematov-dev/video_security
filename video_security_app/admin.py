from django.contrib import admin
from video_security_app.models import Video,Worker
from django.contrib.auth.admin import UserAdmin

@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = ("username", "email", "is_staff", "is_superuser")
    search_fields = ("username", "email")
    ordering = ("username",)

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email", "phone_number", "description")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
    )

    def save_model(self, request, obj, form, change):
        if not change or "password1" in form.changed_data:
            obj.set_password(form.cleaned_data["password1"])
        super().save_model(request, obj, form, change)

admin.site.register([Video])
