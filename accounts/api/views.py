from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from dj_rest_auth.registration.views import VerifyEmailView
from django.utils.translation import ugettext_lazy as _

Player = get_user_model()


@api_view()
def null_view(request):
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view()
def complete_view(request):
    return Response("Email account is activated", status=status.HTTP_200_OK)


class CustomVerifyEmailView(VerifyEmailView):

    def post(self, request, *args, **kwargs):
        # super(CustomVerifyEmailView, self).post(request, *args, **kwargs)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.kwargs['key'] = serializer.validated_data['key']
        confirmation = self.get_object()
        confirmation.confirm(self.request)
        return Response({'detail': _('ok')}, status=status.HTTP_200_OK)
