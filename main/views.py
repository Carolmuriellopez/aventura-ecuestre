from decouple import config
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.sitemaps.views import sitemap as django_sitemap
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from .forms import ContactForm

import logging
from smtplib import SMTPException
from socket import timeout as SocketTimeout

logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def activities(request):
    return render(request, 'main/activities.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                email = EmailMessage(
                subject=f"Consulta web - {form.cleaned_data['name']}",
                body=f"""
                    Nombre: {form.cleaned_data['name']}
                    Email: {form.cleaned_data['email']}
                    Teléfono: {form.cleaned_data['phone']}
                    Idioma: {form.cleaned_data['language']}
                    Actividad: {form.cleaned_data['activity']}
                    Fecha: {form.cleaned_data['date']}
                    Personas: {form.cleaned_data['people']}
                    Mensaje: {form.cleaned_data['message']}
                    """,
                from_email=config('EMAIL_HOST_USER'),
                to=[settings.CONTACT_EMAIL_RECIPIENT],
                reply_to=[form.cleaned_data['email']],
                )
                email.send()
            except (SMTPException, SocketTimeout, OSError) as e:
                logger.error(f"Error al enviar email de contacto: {e}")
                return render(request, 'main/contact.html', {
                    'form': form,
                    'email_error': True,
                })
            return redirect('contacto_gracias')
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})

def aviso(request):
    return render(request, 'main/aviso.html')

def cookies(request):
    return render(request, 'main/cookies.html')

def privacidad(request):
    return render(request, 'main/privacidad.html')

def contacto_gracias(request):
    return render(request, 'main/contacto_gracias.html')

def sitemap_view(request, sitemaps):
    response = django_sitemap(request, sitemaps)
    del response['X-Robots-Tag']
    return response

