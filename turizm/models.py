from email.policy import default
from django.db import models

# Create your models here.

class AboutImages(models.Model):
    photo_name = models.CharField(max_length = 30,default='')
    photo_file = models.ImageField(upload_to = 'about_image/',null=False,blank=False)
    added_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.photo_name


class AboutPage(models.Model):
    title = models.CharField(max_length = 10000,default='',blank=False)
    photo_files = models.ManyToManyField(AboutImages,related_name='photo_files',blank=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class OpenAndCloseHour(models.Model):
    open_hour = models.TimeField()
    close_hour = models.TimeField()
    opan_close_day = models.CharField(max_length = 70)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.opan_close_day

class Rooms(models.Model):
    room_name = models.CharField(max_length = 250)
    room_title = models.CharField(max_length = 1000)
    room_price = models.FloatField()
    room_file = models.ImageField(upload_to = 'room_image/',null=False,blank=False)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.room_name


class MealChoice(models.IntegerChoices):
    HOTDISH = 0, 'HOTDISH'
    DESSERT = 1, 'DESSERT'
    
class MealModel(models.Model):
    meal_name = models.CharField(max_length = 100)
    meal_title = models.CharField(max_length = 100)
    meal_price = models.FloatField()
    user_role = models.IntegerField(choices=MealChoice.choices, default=MealChoice.HOTDISH)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.meal_name


class HotelRoomImage(models.Model):
    hotel_room_image = models.ImageField(upload_to = 'hotel_room_image/',null=False,blank=False)
    hotel_room_name = models.CharField(max_length = 100)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hotel_room_name

class CustomerMassage(models.Model):
    name = models.CharField(max_length = 150,default='')
    email = models.EmailField(max_length = 150,default='')
    phone_nomer = models.IntegerField(default=0,null=False,blank=True)
    message = models.CharField(max_length = 1000,default = '')
    added_at = models.DateTimeField(auto_now_add=True)

class HotelLocationModel(models.Model):
    hotel_name =  models.CharField(max_length = 150,default='')
    hotel_location =  models.CharField(max_length = 150,default='')
    hotel_phone =  models.IntegerField(default=0,null=False,blank=True)
    hotel_email =  models.EmailField(default=0,null=False,blank=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hotel_name
