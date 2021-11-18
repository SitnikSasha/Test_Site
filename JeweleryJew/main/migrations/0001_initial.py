# Generated by Django 3.2.9 on 2021-11-18 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Категория')),
                ('slug', models.SlugField(verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория изделия',
                'verbose_name_plural': 'Категории изделий',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.IntegerField(verbose_name='Артикул')),
                ('title', models.CharField(max_length=40, verbose_name='Изделие')),
                ('slug', models.SlugField(verbose_name='URL')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('img', models.ImageField(height_field=400, upload_to='', verbose_name='Фото товара', width_field=600)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.categoryitem')),
            ],
        ),
    ]