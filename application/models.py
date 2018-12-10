from django.db import models
from accounts.models import User, UserProfile


# Create your models here.
class School(models.Model):
    user = models.ForeignKey(User)
    school_type = (
            ('Pu', 'Public'),
            ('Pi', 'Private'),
            ('Ho', 'Home School'),
        )
    type = models.CharField(max_length=2, choices=school_type, default='Pu')
    school_name = models.CharField(max_length=100, default='')
    grade = models.FloatField(max_length=4.0)

    def __str__(self):
        return self.school_name + "of" + self.user.username;


class Parent(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    cell_phone = models.BigIntegerField(default=0)
    home_phone = models.BigIntegerField(default=0, blank=True)
    work_phone = models.BigIntegerField(default=0, blank=True)

    def __str__(self):
        return self.user.username + "'s parent"


class Application(models.Model):
    user = models.ForeignKey(User)
    user_profile = models.ForeignKey(UserProfile)
    status = (
        ('P', 'Pending'),('A', 'Approved')
    )
    application_status = models.CharField(max_length=1,choices=status, default='P')

    def __str__(self):
        return self.user.username + "'s application"
