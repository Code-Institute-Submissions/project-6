
# Setting for local testing with hardcoded values
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
# (not a production key)
SECRET_KEY = 'vl56)n*7)1-w-uu0vkylyp!s1z+_zcalb-7$*0!o!b5bei$tq='

# Put your local host IP address here
ALLOWED_HOSTS = ["127.0.0.1"]


# EMAIL_BACKEND
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

