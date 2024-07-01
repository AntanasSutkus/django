# Generated by Django 5.0.6 on 2024-06-26 17:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examination', '0005_alter_exam_topic_examresult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='topic',
            field=models.CharField(choices=[('animals', 'gyvunai'), ('KET', 'keliu eimo taisykles'), ('flowers', 'geles')], max_length=200),
        ),
        migrations.CreateModel(
            name='TestQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.question')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.exam')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
