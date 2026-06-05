from django import forms
from django.core.validators import RegexValidator
from django.utils import timezone

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={'placeholder': 'Tu nombre'}),
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'correo@ejemplo'}),
    )
    phone = forms.CharField(
        max_length=20, 
        required=False, 
        widget=forms.TextInput(attrs={'placeholder': '+34 600 000 000'}),
        validators=[
            RegexValidator(
                regex=r'^\+?[\d\s\-]{7,20}$',
                message="Introduce un número de teléfono válido."
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
            ('', 'Elija una actividad'),
            ('pony', 'Pony'),
            ('principiante', 'Principiante'),
            ('playaypinar', 'Playa y pinar'),
            ('lances3', 'Lances 3h'),
            ('lances4', 'Lances 4h'),
            ('pack1', 'Pack 1: holidays'),
            ('pack2', 'Pack 2: week'),
            ('pupilo', 'Pupilaje'),
            ('others', 'Otros')
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
            ('', '¿Cuántos son?'),
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
        widget=forms.Textarea(attrs={'placeholder': 'Para ir organizando la salida, cuéntanos algo sobre vuestra experiencia, nivel de los jinetes, si hay niños, peso y altura. Buscaremos los caballos que mejor se adapten a cada jinete.'}), 
    )

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date and date < timezone.now().date():
            raise forms.ValidationError("La fecha no puede ser anterior a hoy.")
        return date