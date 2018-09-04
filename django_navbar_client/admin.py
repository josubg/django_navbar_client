from django.contrib import admin
from oauth_client.models import AuthProfile
# Register your models here.


@admin.register(AuthProfile)
class AuthProfileAdmin(admin.ModelAdmin):
    pass
