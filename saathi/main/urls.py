from django.urls import path, include
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.HomePageView, name='home'),
    path('home/', views.HomePageView),
    path('about/', views.AboutView, name='about'),
    path('contact/', views.ContactView, name='contact'),
    path('predictions/', views.PredictionsView, name='predictions'),
    path('found/', views.FoundView, name='found'),
]
