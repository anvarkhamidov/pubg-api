from django.shortcuts import render


def index_view(request):
    return render(request, "base.html")