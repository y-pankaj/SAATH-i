from django.urls import include, path
from . import views

urlpatterns = [
    path('Kerala_Floods/', views.Kerala_FloodsView, name='kerala_floods'),
    path('Cyclone_Titli/', views.Cyclone_TitliView, name='cyclone_titli'),
    path('Indonesian_Tsunami/', views.Indonesian_TsunamiView, name='Indonesian_Tsunami'),
    path('Hurricane_Michael/', views.Hurricane_MichaelView, name='Hurricane_Michael'),
]