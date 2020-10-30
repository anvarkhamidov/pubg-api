from django.urls import path, include
from django.contrib.auth.views import PasswordResetConfirmView
from accounts.api import views

urlpatterns = [
    # Override urls
    path('registration/account-email-verification-sent/', views.null_view, name='account_email_verification_sent'),
    path('registration/complete/', views.complete_view, name='account_confirm_complete'),
    path('registration/verify-email/', views.CustomVerifyEmailView.as_view(), name='rest_verify_email'),
    path('password-reset/confirm/<str:uidb64>/<str:token>/', PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password-reset/complete/', views.complete_view, name='password_reset_complete'),
    path('verification-tokens/', views.ListVerificationTokens.as_view(), name='verification-tokens-list'),

    # Default urls
    path('', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls'))
]
