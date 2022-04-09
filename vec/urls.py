
from django.urls import path 
from .views import index

app_name = 'vec'
urlpatterns = [

    path('',index,name='index'),
]
