"""singh2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from pawar2.views import*
from pawar2.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index,name="index"),
    path("about/",about,name='about'),
    path("Services/",services,name='Services'),
    path("Feedback/",Feedback,name='Feedback'),
    path("login/",index1,name='index12'),
    path("form1/",form,name="regform"),
    path("bodybuild/",bodybuild,name="bodybuild"),
    path("crossfit/",crossfit,name='crossfit'),
    path('functional/',functional,name='functional'),
    path('fittraining/',fittraining,name='fittraining'),
    path('yoga/',yoga,name='yoga'),
    path('zumba/',zumba,name='zumba'),
    path('fitnesstrain/',fitnesstrain,name='fitnesstrain'),
    path('cardio/',cardio,name='cardio'),
    path('adredirect/',adredirect,name='adredirect'),
    path("gal/",gal,name='gal'),
    path('che/',che,name='che'),
    path('newnav/',newnav,name='newnav'),
    path('userinfo',userinf,name='userinfo'),
    path('prajjwal/',prajjwal1,name='prajinfo'),
    path('certificate/',certify,name='certificate2'),
    path('cirgen/',cirgen,name='cirgen'),
    path('price/',price2,name='pricing'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
