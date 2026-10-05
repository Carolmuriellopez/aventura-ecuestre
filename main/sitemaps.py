from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'monthly'
    i18n = True
    alternates = True
    x_default = True

    def items(self):
        # nombres de tus URLs en urls.py
        return ['home', 'about', 'activities', 'contact', 'aviso', 'cookies', 'privacidad']

    def location(self, item):
        return reverse(item)