from django.urls import path
from .views import python_link_shortener_online



urlpatterns = [
    
    path('python_link_shortener_online/', python_link_shortener_online, name='python_link_shortener_online'),
    
]