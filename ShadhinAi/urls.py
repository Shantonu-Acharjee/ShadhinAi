from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from base.sitemap import BlogSitemap, CategorySitemap, TagSitemap, UserSitemap, HomePageSitemap, StaticSitemap

from django.shortcuts import render, redirect
from django.views.generic.base import RedirectView

sitemaps = {
    'homepage' : HomePageSitemap,
    'blog' : BlogSitemap, 
    'category' : CategorySitemap,
    'tag' : TagSitemap,
    'user' : UserSitemap,
    'static' : StaticSitemap,
}

def handling_404(request, exception):
    return redirect('home')

urlpatterns = [
    path("admin/", admin.site.urls),
    #path('', include('base.urls')),
    #path('', include('post.urls')),
    #path('', include('user_profile.urls')),
    #path('', include('project.urls')),
    #path('sitemap.xml', sitemap, {'sitemaps' : sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('', RedirectView.as_view(url='https://shadhinai.com'), name= 'home')

] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = handling_404