from django.urls import path, include
from django.conf import settings
from . import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'main'
urlpatterns = [
    path('', views.HomePageView, name='home'),
    path('home/', views.HomePageView),
    path('about/', views.AboutView, name='about'),
    path('contact/', views.ContactView, name='contact'),
    path('predictions/', views.PredictionsView, name='predictions'),
    path('found/', views.FoundView, name='found'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)