from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Lesson
from .forms import LessonForm
from datetime import datetime, timedelta, time
import pytz


def book_lesson(request):
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']
            lesson_start_time = time.fromisoformat(start_time)
            lesson_end_time = time.fromisoformat(end_time)
            lesson_start_datetime = datetime.combine(
                date, lesson_start_time).replace(tzinfo=pytz.UTC)
            lesson_end_datetime = datetime.combine(
                date, lesson_end_time).replace(tzinfo=pytz.UTC)

            lesson_duration = lesson_end_datetime - lesson_start_datetime
            if lesson_duration < timedelta(hours=1):
                form.add_error(
                    'end_time', 'Lesson duration must be at least 1 hour.')
            else:
                existing_lessons = Lesson.objects.filter(
                    start_time__lte=lesson_end_datetime, end_time__gte=lesson_start_datetime)
                if existing_lessons.exists():
                    form.add_error(
                        'start_time', 'This time slot is already booked.')
                else:
                    lesson = form.save(commit=False)
                    lesson.user = request.user
                    lesson.start_time = lesson_start_datetime
                    lesson.end_time = lesson_end_datetime
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
