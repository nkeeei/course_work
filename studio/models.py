from django.db import models
from django.contrib.auth.models import User


class Studio(models.Model):
    """ Студия звукозаписи """
    name = models.CharField(max_length=20,blank=True,null=True,default=None)
    description = models.TextField(blank=True, null=True,default=None)
    address = models.CharField(max_length=128, blank=True,null=True,default=None)
    phone_number = models.CharField(max_length=64, blank=True,null=True,default=None)
    work_time = models.CharField(max_length=128, blank=True,null=True,default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)
    opening_days_hours = models.CharField(max_length=128, blank=True,null=True,default=None)

    def __str__(self):
        return "Студия звукозаписи '%s'" % self.name

    class Meta:
        verbose_name = 'Студия звукозаписи'
        verbose_name_plural = 'Студии звукозаписи'


class StudioImage(models.Model):
    """ Фотографии студии звукозаписи"""
    studio = models.ForeignKey(Studio, on_delete=models.DO_NOTHING,blank=True,null=True,default=None)
    image = models.ImageField(upload_to='studio_images')
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)

    def __str__(self):
        return "%s" % self.studio.name

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class Equipment(models.Model):
    """ Оборудование """
    name = models.CharField(max_length=50,blank=True,null=True,default=None)
    description = models.TextField(blank=True,null=True,default=None)
    image = models.ImageField(upload_to='equipment_image')
    studio = models.ForeignKey(Studio,on_delete=models.DO_NOTHING, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)

    def __str__(self):
        return "'%s'" % self.name

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'


class SoundEngineer(models.Model):
    """ Звуковой инженер """
    name = models.CharField(max_length=20,blank=True,null=True,default=None)
    description = models.TextField(blank=True,null=True,default=None)
    image = models.ImageField(upload_to='sound_engineer_image')
    studio = models.ForeignKey(Studio,on_delete=models.DO_NOTHING,blank=True,null=True,default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)
    quote = models.CharField(max_length=100,blank=True,null=True,default=None)

    def __str__(self):
        return "'%s'" % self.name

    class Meta:
        verbose_name = 'Звуковой инженер'
        verbose_name_plural = 'Звуковые инженеры'


class Service(models.Model):
    """ Услуги """
    name = models.CharField(max_length=20,blank=True,null=True,default=None)
    description = models.TextField(blank=True,null=True,default=None)
    image = models.ImageField(upload_to='service_image')
    studio = models.ForeignKey(Studio,on_delete=models.DO_NOTHING,blank=True,null=True,default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return "'%s'" % self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Event(models.Model):
    """ Мероприятие """
    name = models.CharField(max_length=20,blank=True,null=True,default=None)
    description = models.TextField(blank=True,null=True,default=None)
    image = models.ImageField(upload_to='event_image')
    date = models.DateTimeField(blank=True,null=True)
    location = models.CharField(max_length=50, blank=True, null=True, default=None)
    studio = models.ForeignKey(Studio,on_delete=models.DO_NOTHING,blank=True,null=True,default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return "'%s'" % self.name

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'


class StudioSession(models.Model):
    """ Студийные сессии"""
    studio = models.ForeignKey(Studio, on_delete=models.DO_NOTHING,blank=True,null=True,default=None)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING,blank=True,null=True,default=None)
    date = models.DateField(auto_now_add=False,auto_now=False)
    time = models.CharField(max_length=10,blank=True,null=True,default=None)
    count_hours = models.CharField(max_length=10,blank=True,null=True,default=None)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return "'%s' %s %s" % (self.user,self.date,self.time)

    class Meta:
        verbose_name = 'Студийная сессия'
        verbose_name_plural = 'Студийные сессии'