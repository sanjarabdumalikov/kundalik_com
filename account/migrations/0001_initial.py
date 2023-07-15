# Generated by Django 4.2.1 on 2023-07-14 04:53

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('roles', models.CharField(choices=[('a', 'Admin'), ('s', 'Student'), ('t', 'Teacher'), ('p', 'Parent')], max_length=1)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=65)),
                ('fname', models.CharField(default='', max_length=65)),
                ('date_of_birth', models.DateField(default=datetime.datetime.now)),
                ('address', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('username', models.CharField(default='', max_length=25)),
                ('password', models.CharField(default='', max_length=65)),
                ('phone', models.CharField(default='', max_length=65)),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='TeacherModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=65)),
                ('fname', models.CharField(default='', max_length=65)),
                ('date_of_birth', models.DateField(default=datetime.datetime.now)),
                ('address', models.TextField()),
                ('toifa', models.CharField(default='', max_length=65)),
                ('salary', models.PositiveIntegerField(default=1)),
                ('school', models.ManyToManyField(to='school.schoolmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
