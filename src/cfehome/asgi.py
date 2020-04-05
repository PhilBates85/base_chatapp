import os
import django
from channels.routing import get_default_application

os.enviorn.setdefault("DJANGO_SETTINGS_MODULE", "cfehome.settings")
django.setup()
application = get_default_application()

