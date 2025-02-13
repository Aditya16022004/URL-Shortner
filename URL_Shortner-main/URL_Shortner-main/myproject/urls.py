"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('url_short/',include('url_shortner.urls')),
]



# And, at the end of the file, add a pattern to include the login and logout views for the browsable API.
urlpatterns+=[
    path('api-auth/', include('rest_framework.urls'))
]

'''
If you open a browser and navigate to the browsable API at the moment, you'll find that you're no longer able to create new code snippets. In order to do so we'd need to be able to login as a user.

We can add a login view for use with the browsable API, by editing the URLconf in our project-level urls.py file.'''


'''
The 'api-auth/' part of pattern can actually be whatever URL you want to use.

Now if you open up the browser again and refresh the page you'll see a 'Login' link in the top right of the page. If you log in as one of the users you created earlier, you'll be able to create code snippets again.

Once you've created a few code snippets, navigate to the '/users/' endpoint, and notice that the representation includes a list of the snippet ids that are associated with each user, in each user's 'snippets' field.'''