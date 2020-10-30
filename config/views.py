from django.shortcuts import render
from rest_framework import authentication, permissions
from rest_framework.views import APIView


def index_view(request):
    return render(request, "base.html")


class APIViewMixin(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
