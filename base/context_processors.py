from .models import HeaderLogo



def get_header_logo(request):
    logo = HeaderLogo.objects.first()
    context ={
        "logo" : logo
    }

    return context