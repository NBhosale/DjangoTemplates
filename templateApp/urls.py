from django.urls import path
from templateApp import views



urlpatterns = [
    path('index/', views.index, name='index'),
    path('other/', views.other, name='other'),
    path('relativeUrl/', views.relativeURL, name='relativeUrl'),

]