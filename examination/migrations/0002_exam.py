# Generated by Django 5.0.6 on 2024-06-17 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examination', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('topic', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
