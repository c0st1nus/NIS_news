"""
URL configuration for NIS_news project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    
Add an import:  from my_app import views
Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    
Add an import:  from other_app.views import Home
Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    
Import the include() function: from django.urls import include, path
Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from site_back.views import index, tag_viev, article, admission

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='main'),
    path('news/', index, name='news'),
    path('admission/', admission, name='admission'),
    path('media_club/', index, name='media_club'),
    path('tags/<str:tag>/', tag_viev, name='tags'),
    path('article/<int:article_id>/', article, name='article'),
]