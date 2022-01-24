from django.forms import ModelForm
from .models import Projects, Task, Specialist


class TaskTableForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'task_status']


class ProjectsForm(ModelForm):
    class Meta:
        model = Projects
        fields = '__all__'


class SpecialistForm(ModelForm):
    class Meta:
        model = Specialist
        fields = '__all__'
        exclude = ['user']
