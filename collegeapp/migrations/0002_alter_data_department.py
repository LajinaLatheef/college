# Generated by Django 4.2 on 2023-04-30 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='department',
            field=models.CharField(choices=[('Co', 'Computer Science'), ('Com', 'Commerce'), ('M', 'Mathematics'), ('Mic', 'Microbiology'), ('E', 'English')], default='Co', max_length=10),
        ),
    ]
