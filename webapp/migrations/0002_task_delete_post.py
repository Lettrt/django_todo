# Generated by Django 4.2.3 on 2023-08-06 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Описание')),
                ('status', models.CharField(choices=[('new', 'новая'), ('in_progress', 'в процессе'), ('done', 'выполнено')], default='new', max_length=15, verbose_name='Статус')),
                ('completion_date', models.DateField(blank=True, null=True, verbose_name='Дата выполнения')),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]