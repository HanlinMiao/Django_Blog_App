# Generated by Django 3.0.8 on 2020-07-13 16:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photo', '0004_auto_20200712_2004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='Like', max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='photo',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='likes',
        ),
        migrations.AddField(
            model_name='photo',
            name='liked',
            field=models.ManyToManyField(blank=True, default=None, related_name='usertophoto', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='photo',
            name='author',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, related_name='authortophoto', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Preference',
        ),
        migrations.AddField(
            model_name='like',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photo.photo'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]