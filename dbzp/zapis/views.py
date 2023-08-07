from django.shortcuts import render, redirect
from django.db.models import F
from .models import *
from .forms import *
from django.http import HttpResponse


def index(request):
    disc = Disciplines.objects.all()
    context = {'disc':disc}
    return render(request, 'zapis/index.html', context=context)


def add_discipline(request):
    if request.method == 'POST':
        form = DisciplinesAdd(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
        else:
            return render(request, 'zapis/add_discipline.html', context=context)
    else:
        form = DisciplinesAdd()
        context = {'form':form}
        return render(request, 'zapis/add_discipline.html', context=context)



             
     

def show_notes(request):
    notes = Note.objects.order_by('id')
    context = {'note':notes}
    return render(request, 'zapis/notes.html', context=context)

def add_talon(request, note_id):
    form =StudentNoteAdd()
    if request.method == 'POST':
        form =StudentNoteAdd(request.POST)
        StudentNote.objects.create(surname = request.POST.get('surname'),
                                   name = request.POST.get('name'),
                                   particular = request.POST.get('particular'),
                                   discipline_note_id = note_id)
        Note.objects.values().filter(id = note_id).update(places = F("places") - 1)
        return redirect(show_notes)
    else:
        return render(request, 'zapis/note_add.html', {'form':form})

def add_note(request):
    if request.method == 'POST':
        form = NoteAdd(request.POST)
        if form.is_valid():
            form.save()
            return redirect(show_notes)
        else:
            return render(request, 'zapis/note_add.html', context=context)
    else:
        form = NoteAdd()
        context = {'form':form}
        return render(request, 'zapis/note_add.html', context=context)


def student_list(request):
    stud_list = StudentNote.objects.all()
    return render(request, 'zapis/student_list.html', context={'note':stud_list})
