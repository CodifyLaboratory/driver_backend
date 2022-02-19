# Generated by Django 4.0.2 on 2022-02-19 11:55

from django.db import migrations, models
import news.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('shot_description', models.CharField(max_length=300, null=True)),
                ('text', models.CharField(max_length=2000)),
                ('image', models.ImageField(null=True, upload_to=news.models.image_save_path)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created_date',),
            },
        ),
    ]
