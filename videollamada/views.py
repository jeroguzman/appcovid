from django.shortcuts import render


def videollamada(request):
    return render(request, 'videollamada.html')

def success(request):
    return render(request, 'success.html')


