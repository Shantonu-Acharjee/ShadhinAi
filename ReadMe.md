http://127.0.0.1:8000/static/1.webp
<img src="/media/compressed/{{blog.banner}}" alt="{{blog.title}}">
{{blog.tags.all.title}}
{% for blog in blogs|slice:"6" %}
10.0.0.174:5500



# Alrady done
- sitemap.xml file
- canonical tag (https://{yourdomain})



# I have t do 
- Add bangla sligify
- cheek custom slag
- if title slag is not avable avable it show to provide custom slug
- update post page tage not workong
- only admin can post user can comment user post should be aproveable
- comment section link will not follow/working
- I can't follow myself
- have to add most view post / most propular post
- have to create notificashon for comments
- i have to use page not found 
- i have to use custom sitemap.xml
- tag is not editable problem solve
- forgot password
- title on img tag




# Comands
- python manage.py makemigrations
- python manage.py migrate
- python manage.py startapp notification
- virtualenv env
- pip install django
- pip install pillow
- pip install django-ckeditor
- pip freeze > requirements.txt
- pip3.8 install --user pythonanywhere
- git pull
- rm -r folder name (to deleate a folder)
- git pull --no-edit
- pip install pyshorteners
- exit [n]
- pip install django-autoslug
- pip install -r requirements.txt


# Doc
- Shantonu560634
- https://www.pythonanywhere.com/user/ShantonuAcharjee/consoles/28165668/
- https://cdn.jsdelivr.net/gh/user/repo@version/file
- https://cdn.jsdelivr.net/gh/Shantonu-Acharjee/ShadhinAi.com@main/style.css
- https://cdn.jsdelivr.net/gh/ShadhinAi/ShadhinAi@main/public/static/css/style.css
- (shantonuacharjee.pythonanywhere.com) 09:04 ~/shantonuacharjee.pythonanywhere.com (main)$ 
- <link rel="stylesheet" href="{% static 'static/css/style.css' %}">  
- <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/ShadhinAi/ShadhinAi@main/public/static/css/style.css">
- <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/ShadhinAi/ShadhinAi@main/public/static/css/media.css">
- {% block meta_description %}{% endblock meta_description %}
- {% block schema %}{% endblock schema %}
- <p>{{blog.description|safe}}</p>
- {% block meta_all_details %}{% endblock meta_all_details %}
- https://github.com/MoinulHossainNabil/Blog-Website-Django-Tutorials-Youtube












import os
import sys


sys.path.insert(0, os.path.dirname(__file__))


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    message = 'It works!\n'
    version = 'Python %s\n' % sys.version.split()[0]
    response = '\n'.join([message, version])
    return [response.encode()]


