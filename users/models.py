from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Users(AbstractUser):
    image=models.ImageField(upload_to='users/images/')

    def __str__(self):
        return self.username
    


class UserProfile(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=100)
    # Boshqa kerakli ma'lumotlar
