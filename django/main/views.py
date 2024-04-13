from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def dialog(request):
    return render(request, 'dialog_template.html')


def create_meet(request):
    return render(request, 'meet.html')