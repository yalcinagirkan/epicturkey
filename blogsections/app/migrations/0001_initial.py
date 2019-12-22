# Generated by Django 2.2.6 on 2019-12-21 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content', models.TextField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('cover', models.ImageField(upload_to='img/')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content', models.TextField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('cover', models.ImageField(upload_to='img/')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateField()),
                ('headline', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.City')),
            ],
        ),
    ]
