# This is just a practice. The way neon.com provides the database configuration for Django.

DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.postgresql",
        'NAME': 'django',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'USER': 'django',
        'PASSWORD': 'django',
    }
}
