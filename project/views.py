from django.shortcuts import render
from .forms import TextForm
from project.projects_list.python_link_shortener_online.main_app import PythonLinkShortenerOnline


def python_link_shortener_online(request):
    short_link = ''
    text = ''

    if request.method == 'POST':

        form = TextForm(request.POST)
        
        if form.is_valid():

            try:
                text = form.cleaned_data.get('text')
                short_link = PythonLinkShortenerOnline(text)
                short_link = short_link.short_link_url

            except:
                short_link = 'Plese try again'


    context = {

        "short_link" : short_link,
        'text' : text,

    }
            

    return render(request, 'projects/python_link_shortener_online/index.html', context)