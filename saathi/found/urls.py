from django.urls import path, include
from . import views
from django.conf import settings

app_name = 'found'
urlpatterns = [
    path('kerala_floods/', views.KeralaFloods, name = 'kerala_floods'),
    path('hurricane_michael/', views.HurricaneMichael, name='hurricane_michael'),
    path('cyclone_titli/', views.CycloneTitli, name='cyclone_titli'),
    path('indonesian_tsunami/', views.IndonesianTsunami, name='indonesian_tsunami'),
]
