from .models import HeaderLogo
from django.contrib.sites.shortcuts import get_current_site
from django.utils.functional import SimpleLazyObject



def get_header_logo(request):
    logo = HeaderLogo.objects.first()
    context ={
        "logo" : logo
    }

    return context



def get_site_domain(request):
    site_domain =  SimpleLazyObject(lambda: get_current_site(request))

    context ={
        "site_domain" : site_domain
    }

    return context






