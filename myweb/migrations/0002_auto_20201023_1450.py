# Generated by Django 2.2.7 on 2020-10-23 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Exercise_name', models.CharField(blank=True, max_length=200)),
                ('Exercise_text', models.CharField(blank=True, max_length=200)),
                ('Exercise_time', models.CharField(blank=True, max_length=200)),
                ('Exercise_calorie', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_text', models.CharField(blank=True, max_length=200)),
                ('Raw_text', models.CharField(blank=True, max_length=200)),
                ('How_text', models.CharField(blank=True, max_length=200)),
                ('Calorie_text', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
