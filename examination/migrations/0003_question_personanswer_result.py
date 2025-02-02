# Generated by Django 5.0.6 on 2024-06-18 16:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examination', '0002_exam'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('difficulty', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PersonAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answers', models.CharField(max_length=200)),
                ('correct', models.BooleanField(default=True)),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.question')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answers_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.personanswer')),
                ('exam_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.exam')),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.person')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.question')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
