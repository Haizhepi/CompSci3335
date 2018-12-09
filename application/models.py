from django.db import models
from accounts.models import User, UserProfile


# Create your models here.
class School(models.Model):
    school_type = (
            ('Pu', 'Yes'),
            ('Pi', 'No'),
            ('Ho', 'Unsure'),
        )
    type = models.CharField(max_length=2, choices=school_type, default='Pu')
    school_name = models.CharField(max_length=100, default='')
    grade = models.FloatField(max_length=4.0)


class Application(models.Model):
    user = models.OneToOneField(User)
    user_profile = models.OneToOneField(UserProfile)

    def __str__(self):
        return self.user.username + "'s application"
