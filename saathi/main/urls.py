from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.HomePageView, name='home'),
    path('home/', views.HomePageView),
    path('about/', views.AboutView, name='about'),
    path('contact/', views.ContactView, name='contact'),
    path('predictions/', views.PredictionsView, name='predictions'),
]