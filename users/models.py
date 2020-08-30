from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='def_avatar.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            if img.height < img.width:
                left = (img.width - img.height) / 2
                right = img.width - left
                top = 0
                bottom = img.height
            else:
                top = (img.height - img.width) / 2
                bottom = img.height - top
                left = 0
                right = img.width

            img = img.crop((left, top, right, bottom))
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
