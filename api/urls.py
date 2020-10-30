from django.urls import path, include

urlpatterns = [
    path("accounts/", include("accounts.api.urls")),
    path('', include("tournament.api.urls")),
]
