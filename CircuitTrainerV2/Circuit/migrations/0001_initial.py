# Generated by Django 3.0.5 on 2020-05-05 02:17

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
            name='Routine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Routine_Name', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=500)),
                ('Focus_Group', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('Creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Target_Group', models.CharField(max_length=50)),
                ('Time_Seconds', models.IntegerField(default=0)),
                ('Routine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Circuit.Routine')),
            ],
        ),
    ]
