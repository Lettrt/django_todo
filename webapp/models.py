from django.db import models

status_state = [('new', 'новая'), ('in_progress', 'в процессе'), ('done', 'выполнено')]

class Task(models.Model):
    description = models.TextField('Описание', blank=False)
    status = models.CharField("Статус", max_length=15, choices=status_state, default='new')
    completion_date = models.DateField("Дата выполнения", null=True, blank=True)

    def __str__(self):
        return self.description

