from django.urls import include, path
from . import views

urlpatterns = [
    path('kerala_floods/', views.Kerala_FloodsView, name='kerala_floods'),
    path('cyclone_titli/', views.Cyclone_TitliView, name='cyclone_titli'),
    path('indonesian_tsunami/', views.Indonesian_TsunamiView, name='Indonesian_Tsunami'),
    path('hurricane_michael/', views.Hurricane_MichaelView, name='Hurricane_Michael'),
]