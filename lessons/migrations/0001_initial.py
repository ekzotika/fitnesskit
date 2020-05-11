# Generated by Django 3.0.6 on 2020-05-11 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=250)),
                ('imageUrl', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('place', models.CharField(max_length=500)),
                ('teacher', models.CharField(max_length=100)),
                ('startTime', models.TimeField()),
                ('endTime', models.TimeField()),
                ('weekDay', models.IntegerField()),
                ('appointment_id', models.CharField(max_length=250)),
                ('service_id', models.CharField(max_length=250)),
                ('pay', models.BooleanField()),
                ('appointment', models.BooleanField()),
                ('color', models.CharField(max_length=100)),
                ('availability', models.IntegerField()),
                ('teacher_v2', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lessons.Teacher')),
            ],
        ),
    ]
