from django.db import models


class Disciplines(models.Model):
    disc_name = models.CharField('Название дисциплины', max_length=255)
    tutor = models.CharField('ФИО преподавателя', max_length=255)


    def __str__(self):
        return self.disc_name
    
    class Meta():
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'



class Note(models.Model):
    discipline = models.ForeignKey(Disciplines, verbose_name='Дисциплина', on_delete=models.CASCADE)
    auditor = models.CharField('Аудитория', max_length=255)
    korpus = models.CharField('Корпус', max_length=255)
    time_note = models.TimeField(verbose_name='Время начала')
    date_note = models.DateField(verbose_name='Дата')
    places = models.IntegerField(verbose_name='Количество человек')

    def __str__(self):
        return f'{self.discipline} ({self.date_note})'
    
    class Meta():
        verbose_name = 'Дисциплина (запись)'
        verbose_name_plural = 'Дисциплины (записи)'


class StudentNote(models.Model):
    surname = models.CharField('Фамилия', max_length=255)
    name = models.CharField('Имя', max_length=255)
    particular = models.CharField('Отчество', max_length=255)
    discipline_note = models.ForeignKey(Note, verbose_name='Запись', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.surname} {self.name[0].upper()}. {self.particular[0].upper()}. - {self.discipline_note}'

    class Meta():
        verbose_name = 'Студент - запись'
        verbose_name_plural = 'Студенты - записи'