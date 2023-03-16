from .models import Lesson
from django import forms


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['start_time', 'end_time', 'location']
        widgets = {
            'start_time': forms.TextInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.TextInput(attrs={'type': 'datetime-local'}),
        }
