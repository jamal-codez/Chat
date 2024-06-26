# Generated by Django 4.1 on 2022-09-07 11:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('ph', models.BigIntegerField()),
                ('birth', models.DateField()),
                ('country', models.CharField(max_length=100)),
                ('adrs', models.CharField(blank=True, max_length=100)),
                ('mg', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
