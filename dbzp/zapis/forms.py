from django.forms import ModelForm
from django import forms
from .models import *



class DisciplinesAdd(ModelForm):
    class Meta():
        model = Disciplines
        fields = "__all__"

class NoteAdd(ModelForm):
    class Meta():
        model = Note
        fields = "__all__"


class StudentNoteAdd(forms.Form):
    surname = forms.CharField()
    name = forms.CharField()
    particular = forms.CharField()