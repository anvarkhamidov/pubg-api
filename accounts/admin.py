from django.contrib import admin
from django.contrib.auth.models import Group

from accounts.models import Player, VerificationToken

admin.site.unregister(Group)
admin.site.register(Player)
admin.site.register(VerificationToken)
