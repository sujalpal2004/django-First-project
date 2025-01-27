# Generated by Django 5.1.2 on 2025-01-13 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookatable',
            name='booking_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='bookatable',
            name='booking_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='bookatable',
            name='guest_count',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='bookatable',
            name='phone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=200),
        ),
    ]
