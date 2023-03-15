from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


def book_lesson(request):
    return render(request, 'book_lesson.html')


@login_required
def view_lessons(request):
    return render(request, 'view_lessons.html')
