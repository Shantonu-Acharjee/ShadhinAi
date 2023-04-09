from django.db import models
from django.utils.text import slugify

class Slider(models.Model):
    title = models.CharField(max_length= 150)
    banner = models.ImageField(upload_to = 'slider', null= True, blank= True)
    image_link = models.CharField(max_length= 300, null= True, blank= True)
    destination = models.CharField(max_length= 250, default= '#')
    created_date = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
         self.slug = slugify(self.title)
         super().save(*args, **kwargs)




class HeaderLogo(models.Model):
    brand_name = models.CharField(max_length= 50)
    brang_logo = models.ImageField(upload_to= 'logo', null= True, blank= True)
    image_link = models.CharField(max_length= 300, null= True, blank= True)


class ScrollingText(models.Model):
    text = models.TextField(null= True, blank= True)
