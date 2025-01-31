import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'your-secret-key-here'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangosaml2',  # Add djangosaml2 to installed apps
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Required for sessions
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Required for authentication
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'djangosaml2.middleware.SamlSessionMiddleware',  # Add this for SAML sessions
]

# Root URL configuration
ROOT_URLCONF = 'myproject.urls'  # Ensure this points to your urls.py module

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'

# Database (optional for now)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# SAML Configuration (as provided earlier)
import saml2
from saml2.saml import NAMEID_FORMAT_EMAILADDRESS

SAML_CONFIG = {
    'xmlsec_binary': '/usr/bin/xmlsec1',
    'entityid': 'app1',
    'service': {
        'sp': {
            'endpoints': {
                'assertion_consumer_service': [
                    ('http://localhost:8000/saml2/acs/', saml2.BINDING_HTTP_POST),
                ],
                "single_logout_service": [
                    ("https://localhost:8000/saml2/slo/", saml2.BINDING_HTTP_REDIRECT),
                    ("https://localhost:8000/saml2/slo/", saml2.BINDING_HTTP_POST),
                ],
            },
            'allow_unsolicited': True,
            'authn_requests_signed': True,
            'logout_requests_signed': True,
            'want_assertions_signed': True,
            'want_response_signed': True,
            'signing_algorithm': 'http://www.w3.org/2001/04/xmldsig-more#rsa-sha256',
            'digest_algorithm': 'http://www.w3.org/2001/04/xmlenc#sha256',
            
        },
    },
    'metadata': {
        'local': ['/home/smsrk/keycloak/myproject/idp.xml'],
    },
    'key_file': '/home/smsrk/keycloak/myproject/private.key',
    'cert_file': '/home/smsrk/keycloak/myproject/cert.pem',
#    'encryption_keypairs': [{
#        'key_file': '//home/smsrk/keycloak/myproject/private.key',
#        'cert_file': '/home/smsrk/keycloak/myproject/cert.pem',
#    }],
    'name_id_format': NAMEID_FORMAT_EMAILADDRESS,
}

SAML_ATTRIBUTE_MAPPING = {
#    'username': ('username', 'Username'),
    'email': ('email', 'Email'),
}

SAML_USE_NAME_ID_AS_USERNAME = True

AUTHENTICATION_BACKENDS = [
    'djangosaml2.backends.Saml2Backend',
    'django.contrib.auth.backends.ModelBackend',
]

LOGIN_URL = '/saml2/login/'

