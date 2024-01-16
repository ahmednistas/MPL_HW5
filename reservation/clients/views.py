from django.shortcuts import render


def index(request):
    return render(request, 'info.html')


def info(request):
    return render(request, 'info.html')


def add(request):
    return render(request, 'add.html')