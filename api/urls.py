from django.urls import path, include

urlpatterns = [
    path("accounts/", include("accounts.api.urls")),
    path("tr/", include("tournament.api.urls")),
]
