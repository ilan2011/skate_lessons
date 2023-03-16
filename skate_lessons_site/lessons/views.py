from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Lesson
from .forms import LessonForm
import os


def book_lesson(request):
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.user = request.user
            lesson.save()
            return redirect('view_lessons')
    else:
        form = LessonForm()
    user_authenticated = request.user.is_authenticated
    return render(request, 'book_lesson.html', {'form': form, 'user_authenticated': user_authenticated})


@login_required
def view_lessons(request):
    lessons = Lesson.objects.filter(user=request.user)
    return render(request, 'view_lessons.html', {'lessons': lessons})
