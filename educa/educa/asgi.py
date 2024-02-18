"""
ASGI config for ChatAPI project.
It exposes the ASGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""
'''
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'educa.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    # Adicione rotas de WebSocket aqui, se necessário.
})
'''


"""
https://github.com/django/channels/issues/2035
"""

import os

import django
from channels.routing import get_default_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "educa.settings")
django.setup()
application = get_default_application()