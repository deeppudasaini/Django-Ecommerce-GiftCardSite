from django.contrib import admin
from django.urls import path,include    
from . import views
urlpatterns = [
    path('',views.Index,name="Home"),
    path('cards',views.Card,name="Cards"),
    path('about',views.About,name="About"),
    path('contact',views.Contact,name="Contact"),
    path('index',views.Home,name="Home"),
    path('singleCard/idOfCard=<int:idOfCard>',views.SingleCard,name="Single Card"),
]
