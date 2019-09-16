from django.shortcuts import render


def conferences(request):
    data = {
        'title': 'Конверенции',
    }
    return render(request, 'conferences/conferences.html', data)
