# Generated by Django 4.0.2 on 2022-02-18 10:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=14)),
                ('duration', models.IntegerField()),
                ('max_student', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator])),
            ],
        ),
    ]