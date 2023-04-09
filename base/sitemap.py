from django.contrib.sitemaps import Sitemap
from post.models import Blog, Category, Tag
from user_profile.models import User
from django.urls import reverse



class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Blog.objects.all()
    

    def lastmod(self, obj):
        return obj.updated
    

    def location(self, obj):
        return '/blog/%s' % (obj.slug)
    




class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Category.objects.all()
    

    def lastmod(self, obj):
        return obj.updated
    

    def location(self, obj):
        return '/category/%s' % (obj.slug)
    





class TagSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Tag.objects.all()
    

    def lastmod(self, obj):
        return obj.updated
    

    def location(self, obj):
        return '/tag/%s' % (obj.slug)
    





class UserSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return User.objects.all()
    

    def lastmod(self, obj):
        return obj.updated
    

    def location(self, obj):
        return '/user/%s' % (obj.username)