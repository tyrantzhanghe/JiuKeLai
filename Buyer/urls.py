from django.urls import path,re_path
from Buyer.views import *

urlpatterns=[
    path('index/',index),
    path('login/',login),
]