# Generated by Django 5.0.6 on 2024-06-25 17:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examination', '0004_remove_question_difficulty_question_complexity_level_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='topic',
            field=models.CharField(choices=[('KET', 'keliu eimo taisykles'), ('flowers', 'geles'), ('animals', 'gyvunai')], max_length=200),
        ),
        migrations.CreateModel(
            name='ExamResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.person')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.question')),
                ('question_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.personanswer')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.exam')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
