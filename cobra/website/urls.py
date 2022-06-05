from unicodedata import name
from django.urls import path
from django.contrib import admin
from .views import Kungfu, firstPageView
from .views import my_view
from .views import about,contactus,JoinUs,Karate,Judo
urlpatterns = [
    path('cobra/admin/', admin.site.urls),
    path('first/', firstPageView, name='first_page'),
    path('',my_view,name='index'),
    path('about',about,name='about'),
    path('contactus',contactus,name='contactus'),
    path('joinus',JoinUs,name='joinus'),
    path('karate',Karate,name='karate'),
    path('judo',Judo,name='judo'),
    path('Kungfu',Kungfu,name='kungfu')

]
