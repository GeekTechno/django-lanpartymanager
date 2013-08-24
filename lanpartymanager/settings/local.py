from .core import *


# Debug settings
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Admin and mangager settings
ADMINS = (
    ('Adrian Alexander Eriksen', 'adrianeriksen@users.noreply.github.com'),
)

MANAGERS = ADMINS

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'lpm',
        'USER': 'django',
        'PASSWORD': get_env_variable('PGPASS_DJANGO'),
    }
}