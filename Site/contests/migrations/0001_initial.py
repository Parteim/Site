# Generated by Django 2.2.4 on 2019-09-06 03:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('text', models.TextField()),
                ('img', models.ImageField(default='default/default_contests.jpg', upload_to='contests')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('full_information_about_contest', models.FileField(blank=True, default='', null=True, upload_to='contests/file')),
            ],
        ),
        migrations.CreateModel(
            name='FutureContests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('text', models.TextField()),
                ('img', models.ImageField(default='default/default_contests.jpg', upload_to='contests')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('full_information_about_contest', models.FileField(blank=True, default='', null=True, upload_to='contests/file')),
            ],
        ),
        migrations.CreateModel(
            name='Winners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('img', models.ImageField(default='default/user_profile_img.png', upload_to='contests/winners')),
                ('title_contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contests.Contests')),
            ],
        ),
        migrations.CreateModel(
            name='PastContests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('img', models.ImageField(default='default/default_contests.jpg', upload_to='contests')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contests.Contests')),
                ('winners', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contests.Winners')),
            ],
        ),
    ]
