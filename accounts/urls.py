from .views import *
from django.urls import path
urlpatterns=[
    path('signup/',register,name='signup')

]