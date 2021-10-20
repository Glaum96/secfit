# Generated by Django 3.1 on 2021-10-20 15:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import meals.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('notes', models.TextField()),
                ('calories', models.IntegerField()),
                ('is_veg', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meals', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='MealFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=meals.models.meal_directory_path)),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='meals.meal')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meal_files', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
