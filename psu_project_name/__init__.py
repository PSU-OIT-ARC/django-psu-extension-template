from django.conf import settings
from psu_base.classes.Log import Log
log = Log()

__version__ = '0.0.1'

__all__ = []

# Default settings
_DEFAULTS = {
    # Admin Menu Items
    'PSU_{{ project_name }}_ADMIN_LINKS'.upper(): [
        # {
        #     'url': "{{ project_name }}:{{ project_name }}_index", 'label': "{{ project_name }} Feature", 'icon': "fa-whatever",
        #     'authorities': "admin"
        # },
    ]
}

# Assign default setting values
log.debug("Setting default settings for PSU_{{ project_name }}")
for key, value in list(_DEFAULTS.items()):
    try:
        getattr(settings, key)
    except AttributeError:
        setattr(settings, key, value)
    # Suppress errors from DJANGO_SETTINGS_MODULE not being set
    except ImportError as ee:
        log.debug(f"Error importing {key}: {ee}")
