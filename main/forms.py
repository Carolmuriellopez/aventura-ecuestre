from django import forms
from django.core.validators import RegexValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': _('Tu nombre')}),
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': _('correo@ejemplo')}),
    )
    phone = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '+34 600 000 000'}),
        validators=[
            RegexValidator(
                regex=r'^\+?[\d\s\-]{7,20}$',
                message=_("Introduce un número de teléfono válido.")
            )
        ]
    )
    language = forms.ChoiceField(
        choices=[
            ('es', 'Español'),
            ('en', 'English'),
            ('de', 'Deutsch'),
            ('fr', 'Français'),
        ],
        required=False,
    )
    activity = forms.ChoiceField(
        choices=[
            ('', _('Elija una actividad')),
            ('pony', _('Pony')),
            ('principiante', _('Principiante')),
            ('playaypinar', _('Playa y pinar')),
            ('lances3', _('Lances 3h')),
            ('lances4', _('Lances 4h')),
            ('pack1', _('Pack 1: holidays')),
            ('pack2', _('Pack 2: week')),
            ('pupilo', _('Pupilaje')),
            ('others', _('Otros')),
        ],
    )
    date = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                'placeholder': 'dd/mm/aaaa',
                'type': 'date',
                'min': timezone.now().date().isoformat(),
            }),
    )
    people = forms.ChoiceField(
        choices=[
            ('', _('¿Cuántos son?')),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8)
        ],
        required=False,
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': _('Cuéntanos el nivel de los jinetes, si hay niños, y el peso y altura aproximados. Así podremos asignar el caballo más adecuado para cada uno.')}),
    )

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date and date < timezone.now().date():
            raise forms.ValidationError(_("La fecha no puede ser anterior a hoy."))
        return date
