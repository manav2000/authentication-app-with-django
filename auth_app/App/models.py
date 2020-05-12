from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    SELECT_GENDER = (
        ('0', 'Female'),
        ('1', 'Male'),
        ('2', 'Others')
    )
    gender = models.CharField(choices=SELECT_GENDER,
                              max_length=10)
    nationality = CountryField()

    def __str__(self):
        return str(self.user)
