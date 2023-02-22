# Generated by Django 4.0.1 on 2023-02-17 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_owner', models.IntegerField()),
                ('avatar', models.ImageField(default='defaultimg.png', upload_to='profileimgs')),
                ('description', models.TextField(blank=True)),
                ('loaction', models.CharField(blank=True, max_length=100)),
                ('profile_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
