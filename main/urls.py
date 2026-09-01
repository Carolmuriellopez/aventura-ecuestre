from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quienes-somos/', views.about, name='about'),
    path('actividades/', views.activities, name='activities'),
    path('contacto/', views.contact, name='contact'),
    path('aviso-legal/', views.aviso, name='aviso'),
    path('politica-de-cookies/', views.cookies, name='cookies'),
    path('politica-de-privacidad/', views.privacidad, name='privacidad'),
    path('contacto/gracias/', views.contacto_gracias, name='contacto_gracias'),
]
