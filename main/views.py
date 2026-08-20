from decouple import config
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import ContactForm

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
            send_mail(
                subject=f"Consulta web - {form.cleaned_data['name']}",
                message=f"""
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
                recipient_list=[settings.CONTACT_EMAIL_RECIPIENT],
            )
            return redirect('contacto_gracias')
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form':form})

def aviso(request):
    return render(request, 'main/aviso.html')

def cookies(request):
    return render(request, 'main/cookies.html')

def privacidad(request):
    return render(request, 'main/privacidad.html')

def contacto_gracias(request):
    return render(request, 'main/contacto_gracias.html')

