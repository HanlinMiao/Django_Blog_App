# Generated by Django 3.0.8 on 2020-07-13 00:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photo', '0003_photo_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='photo',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('picture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photo.photo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'picture', 'value')},
            },
        ),
    ]
