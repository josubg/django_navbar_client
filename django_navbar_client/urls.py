from django.urls import path
from oauth_client.views import oauth_callback, oauth_login, oauth_logout, oauth_navbar


app_name = "django_navbar_client"

urlpatterns = [
    path('api/login_callback/', oauth_callback, name="callback"),
    path('view/logout/', oauth_logout, name="logout"),
    path('view/login/', oauth_login, name="logout"),
    path('widget/navbar/', oauth_navbar, name="navbar"),
]