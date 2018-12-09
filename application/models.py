from django.db import models
from accounts.models import User, UserProfile


# Create your models here.
class School(models.Model):
    school_type = (
            ('Pu', 'Public'),
            ('Pi', 'Private'),
            ('Ho', 'Home School'),
        )
    type = models.CharField(max_length=2, choices=school_type, default='Pu')
    school_name = models.CharField(max_length=100, default='')
    grade = models.FloatField(max_length=4.0)


class Application(models.Model):
    user = models.ForeignKey(User)
    user_profile = models.OneToOneField(UserProfile)
    status = (
        ('P', 'Pending'),('A', 'Approved')
    )
    application_status = models.CharField(max_length=1,choices=status, default='P')

    def __str__(self):
        return self.user.username + "'s application"
