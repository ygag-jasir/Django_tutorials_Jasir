import os
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

def user_profile_image_path(instance, filename):
    # Get the user's object ID
    user_id = instance.user.id
    # Construct the file path
    folder_name = f'{user_id}'
    return os.path.join('profile_images', folder_name, filename)

class UserAppModel(models.Model):    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to=user_profile_image_path)    
    