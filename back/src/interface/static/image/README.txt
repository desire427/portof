Placez ici votre fichier photo.png pour qu'il soit accessible dans vos templates Django via la balise :

<img src="{% static 'image/photo.png' %}" ...>

Vérifiez que dans settings.py vous avez bien :

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

Et que l'application 'django.contrib.staticfiles' est bien dans INSTALLED_APPS.

Pour la production, n'oubliez pas de lancer collectstatic.
