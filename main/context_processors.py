from django.conf import settings
from django.utils import translation
from django.urls import NoReverseMatch, resolve
from django.urls import reverse
from django.urls.exceptions import Resolver404
from django.utils import translation

def ga4(request):
    return {'GA4_MEASUREMENT_ID': settings.GA4_MEASUREMENT_ID}

def canonical_path(request):
    """
    request.path with any active language prefix (/en/, /fr/, /de/...)
    stripped off. Needed as the `next` value for the language switcher:
    LocaleMiddleware forces the default language while resolving the
    unprefixed /i18n/setlang/ endpoint, so passing a still-prefixed path
    there makes Django's URL translation silently fail and the switch
    gets ignored. An unprefixed path always resolves correctly.
    """
    path = request.path
    lang = translation.get_language_from_path(path)
    if lang:
        prefix = f'/{lang}'
        if path.startswith(prefix):
            path = path[len(prefix):] or '/'
    return {'CANONICAL_PATH': path}

def hreflang_urls(request):
    try:
        match = resolve(request.path_info)
    except Resolver404:
        return {}
    if not match.url_name:
        return {}
    
    urls = {}
    for lang_code, _ in settings.LANGUAGES:
        try:
            with translation.override(lang_code):
                urls[lang_code] = reverse(match.url_name, args=match.args, kwargs=match.kwargs)
        except NoReverseMatch:
            continue
    return {
        'hreflang_urls': urls,
        'hreflang_default_url': urls.get(settings.LANGUAGE_CODE),
    }