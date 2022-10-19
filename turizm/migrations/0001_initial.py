# Generated by Django 4.1.2 on 2022-10-19 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_name', models.CharField(default='', max_length=30)),
                ('photo_file', models.ImageField(upload_to='about_image/')),
                ('added_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerMassage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150)),
                ('email', models.EmailField(default='', max_length=150)),
                ('phone_nomer', models.IntegerField(blank=True, default=0)),
                ('message', models.CharField(default='', max_length=1000)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='HotelLocationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(default='', max_length=150)),
                ('hotel_location', models.CharField(default='', max_length=150)),
                ('hotel_phone', models.IntegerField(blank=True, default=0)),
                ('hotel_email', models.IntegerField(blank=True, default=0)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='HotelRoomImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_room_image', models.ImageField(upload_to='hotel_room_image/')),
                ('hotel_room_name', models.CharField(max_length=100)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MealModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_name', models.CharField(max_length=100)),
                ('meal_title', models.CharField(max_length=100)),
                ('meal_price', models.FloatField()),
                ('user_role', models.IntegerField(choices=[(0, 'HOTDISH'), (1, 'DESSERT')], default=0)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OpenAndCloseHour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_hour', models.TimeField()),
                ('opan_close_day', models.CharField(max_length=70)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=250)),
                ('room_title', models.CharField(max_length=1000)),
                ('room_price', models.FloatField()),
                ('room_file', models.ImageField(upload_to='room_image/')),
                ('added_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=10000)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('photo_files', models.ManyToManyField(blank=True, related_name='photo_files', to='turizm.aboutimages')),
            ],
        ),
    ]