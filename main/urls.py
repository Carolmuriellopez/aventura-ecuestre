from django.urls import path
from django.contrib.sitemaps.views import sitemap
from . import views
from main.sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}
urlpatterns = [
    path('', views.home, name='home'),
    path('quienes-somos/', views.about, name='about'),
    path('actividades/', views.activities, name='activities'),
    path('contacto/', views.contact, name='contact'),
    path('aviso-legal/', views.aviso, name='aviso'),
    path('politica-de-cookies/', views.cookies, name='cookies'),
    path('politica-de-privacidad/', views.privacidad, name='privacidad'),
    path('contacto/gracias/', views.contacto_gracias, name='contacto_gracias'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
