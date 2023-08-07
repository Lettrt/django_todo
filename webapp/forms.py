from django import forms
from .models import Task, status_state

class TaskForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=forms.Textarea)
    status = forms.ChoiceField(label="Статус", choices=status_state)
    completion_date = forms.DateField(label="Дата выполнения", required=False, widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Task
        fields = ['description', 'status', 'completion_date']