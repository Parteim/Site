from django.shortcuts import render


def exam_page(request):
    data = {
        'title': 'Экзамены'
    }
    return render(request, 'exam/exam_page.html', data)
