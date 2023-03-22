from .models import Lesson
from django import forms
from datetime import date, timedelta


def time_choices():
    times = []
    for hour in range(0, 24):
        for minute in [0, 30]:
            time_str = f"{hour:02d}:{minute:02d}"
            times.append((time_str, time_str))
    return times


class LessonForm(forms.ModelForm):
    LOCATIONS = (
        ('Piedmont Skate Park', 'Piedmont Skate Park'),
        ('Berkeley Skate Park', 'Berkeley Skate Park'),
        ('Emeryville Skatepark', 'Emeryville Skatepark'),
    )

    tomorrow = date.today() + timedelta(days=1)
    date = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(
            attrs={'type': 'date', 'id': 'id_date', 'min': tomorrow.strftime('%Y-%m-%d')})
    )
    start_time = forms.ChoiceField(choices=time_choices(), widget=forms.Select(
        attrs={'id': 'id_start_time', 'disabled': True}))
    end_time = forms.ChoiceField(choices=time_choices(), widget=forms.Select(
        attrs={'id': 'id_end_time', 'disabled': True}))

    location = forms.ChoiceField(choices=LOCATIONS)

    class Meta:
        model = Lesson
        fields = ['date', 'start_time', 'end_time', 'location']
