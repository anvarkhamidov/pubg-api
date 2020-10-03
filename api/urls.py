from django.urls import path, include

urlpatterns = [
    path("accounts/", include("accounts.api.urls")),
    path("tournaments/", include("tournament.api.urls")),
]
