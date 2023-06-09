from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

# Create your models here.


# create model for user
class User(AbstractUser):
    updated = models.DateTimeField(auto_now= True)
    email = models.EmailField(max_length= 150, unique= True, error_messages= {'unique' : 'Email must be unique'})
    profile_image = models.ImageField(upload_to= 'profile_images', null= True, blank= True)
    followers = models.ManyToManyField('Follow')
    REQUIRED_FIELDS = ['email']
    objects = CustomUserManager()

    def __str__(self):
        return self.username
    
    def get_profile_picture(self):
        url = ''
        try:
            url = self.profile_image.url

        except:
            url = ''

        return url
    



class Follow(models.Model):
    followed = models.ForeignKey(User, related_name= 'user_followers', on_delete= models.CASCADE)
    followed_by = models.ForeignKey(User, related_name= 'user_follows', on_delete= models.CASCADE)
    muted = models.BooleanField(default= False)
    created_date = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f"{self.followed_by.username} started following {self.followed.username}"