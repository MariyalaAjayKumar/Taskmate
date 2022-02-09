from django import forms
from todolist_app.models import TaskList

class TaskForm(forms.ModelForm):
    class Meta:
        # meta will use to work to fields
        model = TaskList
        fields= ['task','done']