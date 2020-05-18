# Generated by Django 3.0.5 on 2020-05-17 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_comp_varsity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comp',
            name='event',
        ),
        migrations.RemoveField(
            model_name='comp',
            name='onteam',
        ),
        migrations.RemoveField(
            model_name='round',
            name='aff',
        ),
        migrations.RemoveField(
            model_name='round',
            name='neg',
        ),
        migrations.RemoveField(
            model_name='round',
            name='type',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='location',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='year',
        ),
        migrations.AddField(
            model_name='round',
            name='bracket',
            field=models.CharField(choices=[('PRE', 'Preliminary'), ('OCT', 'Octafinal'), ('QRT', 'Quarterfinal'), ('SEM', 'Semifinal'), ('FIN', 'Final'), ('OTH', 'Other')], default='OTH', max_length=3),
        ),
        migrations.AddField(
            model_name='round',
            name='debater',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Comp'),
        ),
        migrations.AddField(
            model_name='round',
            name='event',
            field=models.CharField(choices=[('VPO', 'Varsity Policy'), ('VLD', 'Varsity Lincoln-Douglas'), ('VPF', 'Public Forum'), ('NPO', 'Novice Policy'), ('NLD', 'Novice Lincoln-Douglas'), ('OTH', 'Other')], default='OTH', max_length=3),
        ),
        migrations.AddField(
            model_name='round',
            name='opponent',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='round',
            name='position',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='round',
            name='won',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tournament',
            name='name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='comp',
            name='name',
            field=models.CharField(default='Unknown', max_length=100, unique=True),
        ),
    ]
