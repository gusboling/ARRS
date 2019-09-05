# Generated by Django 2.2.5 on 2019-09-05 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('event', models.CharField(max_length=100)),
                ('varsity', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('PRE', 'Preliminary'), ('TOC', 'Triple Octafinal'), ('DOC', 'Double Octafinal'), ('OCT', 'Octafinal'), ('QRT', 'Quarterfinal'), ('SEM', 'Semifinal'), ('FIN', 'Final')], default='PRE', max_length=3)),
                ('tournament', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Tournament')),
            ],
        ),
    ]
