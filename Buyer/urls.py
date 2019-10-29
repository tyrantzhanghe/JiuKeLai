from django.urls import path,re_path
from Seller.views import *

urlpatterns=[
    path('index/',index),
    path('login/',login),
]