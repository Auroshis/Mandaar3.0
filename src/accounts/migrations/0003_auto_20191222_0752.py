# Generated by Django 3.0 on 2019-12-22 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191221_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentattendance',
            name='classes_attended2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='studentattendance',
            name='classes_attended3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='studentattendance',
            name='classes_attended4',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='studentattendance',
            name='classes_attended5',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='studentattendance',
            name='classes_attended6',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='studentattendance',
            name='subject2',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='studentattendance',
            name='subject3',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='studentattendance',
            name='subject4',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='studentattendance',
            name='subject5',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='studentattendance',
            name='subject6',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='studentattendance',
            name='total_classes2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='studentattendance',
            name='total_classes3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='studentattendance',
            name='total_classes4',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='studentattendance',
            name='total_classes5',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='studentattendance',
            name='total_classes6',
            field=models.IntegerField(default=0),
        ),
    ]