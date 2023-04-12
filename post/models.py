from django.db import models
from user_profile.models import User
from django.utils.text import slugify
from .slugs import generate_unique_slug
from ckeditor.fields import RichTextField


class Category(models.Model):
    title = models.CharField(max_length= 60, unique= True)
    title_tag = models.CharField(max_length= 150, null= True, blank= True)
    slug = models.SlugField(null= True, blank= True)
    created_date = models.DateField(auto_now_add= True)
    updated = models.DateTimeField(auto_now= True)
    meta_description = models.CharField(max_length= 160, null= True, blank= True)
    banner = models.ImageField(upload_to= 'category_banners', blank= True, null= True)
    high_regulation_banner_link = models.CharField(max_length= 350, null= True, blank= True)
    schema_data = models.TextField(null= True, blank= True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
         self.slug = slugify(self.title)
         super().save(*args, **kwargs)





class Tag(models.Model):
    title = models.CharField(max_length= 60)
    title_tag = models.CharField(max_length= 150, null= True, blank= True)
    slug = models.SlugField(null= True, blank= True)
    created_date = models.DateField(auto_now_add= True)
    updated = models.DateTimeField(auto_now= True)
    meta_description = models.CharField(max_length= 160, null= True, blank= True)
    banner = models.ImageField(upload_to= 'tag_banners', blank= True, null= True)
    high_regulation_banner_link = models.CharField(max_length= 350, null= True, blank= True)
    schema_data = models.TextField(null= True, blank= True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
         self.slug = slugify(self.title)
         super().save(*args, **kwargs)
    





class Blog(models.Model):
    user = models.ForeignKey(User, related_name= 'user_blogs', on_delete= models.CASCADE)
    category = models.ForeignKey(Category, related_name= 'category_blogs', on_delete= models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name= 'tag_blogs', blank= True)
    likes = models.ManyToManyField(User, related_name='user_likes', blank= True)
    title = models.CharField(max_length= 250)
    slug = models.SlugField(allow_unicode=True, null= True, blank= True)
    banner = models.ImageField(upload_to= 'blog_banners', blank= True, null= True)
    low_regulation_banner_link = models.CharField(max_length= 350, null= True, blank= True)
    high_regulation_banner_link = models.CharField(max_length= 350, null= True, blank= True)
    meta_description = models.CharField(max_length= 300, null= True, blank= True)
    description = RichTextField()
    created_date = models.DateField(auto_now_add= True)
    updated = models.DateTimeField(auto_now= True)
    schema_data = models.TextField(null= True, blank= True)

    def __str__(self):
        return self.title
    

    def save(self, *args, **kwargs):
        updating = self.pk is not None

        if not self.slug:
            self.slug = self.title.replace(" ", "-").replace(",", "")
        return super(Blog, self).save(*args, **kwargs)
    
        
        """if updating:
            self.slug = generate_unique_slug(self, self.title, update=True)
            super().save(*args, **kwargs)
        else:
            self.slug = generate_unique_slug(self, self.title)
            super().save(*args, **kwargs)"""
    





    
class Comment(models.Model):
        user = models.ForeignKey(User, related_name= 'user_comments', on_delete= models.CASCADE)
        blog = models.ForeignKey(Blog, related_name= 'blog_comments', on_delete= models.CASCADE)
        text = models.TextField()
        created_date = models.DateTimeField(auto_now_add= True)


        def __str__(self):
            return self.text
        





  
class Reply(models.Model):
        user = models.ForeignKey(User, related_name= 'user_replies', on_delete= models.CASCADE)
        comment = models.ForeignKey(Comment, related_name= 'comment_replies', on_delete= models.CASCADE)
        text = models.TextField()
        created_date = models.DateTimeField(auto_now_add= True)


        def __str__(self):
            return self.text