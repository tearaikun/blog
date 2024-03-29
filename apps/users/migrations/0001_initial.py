# Generated by Django 5.0.1 on 2024-01-29 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=256)),
                ('age', models.PositiveSmallIntegerField()),
                ('job', models.CharField(max_length=256)),
                ('gender', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=13)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('tiktok', models.URLField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('apple_id', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
