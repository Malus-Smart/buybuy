"""
Django settings for buybuy project.
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-your-secret-key-change-in-production'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'crispy_bootstrap5',
    'shop',
    'cart',
    'orders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'buybuy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'buybuy.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Crispy Forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# Cart session ID
CART_SESSION_ID = 'cart'

# Login URLs
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Production settings for Railway/Heroku deployment
import dj_database_url

if os.environ.get('RAILWAY_ENVIRONMENT') or os.environ.get('DYNO'):
    # Production mode - temporarily enable DEBUG to see errors
    DEBUG = True  # Temporarily True for debugging
    ALLOWED_HOSTS = ['*']
    
    # Debug: Print all environment variables that might contain database info
    print("DEBUG: All DATABASE/PG related env vars:")
    for key in os.environ.keys():
        if 'DATA' in key or 'PG' in key or 'POST' in key:
            value = os.environ[key]
            print(f"  {key}: {value[:50]}..." if len(value) > 50 else f"  {key}: {value}")
    
    # Database configuration for Railway/Heroku
    # Try multiple environment variable names
    database_url = (
        os.environ.get('DATABASE_URL') or 
        os.environ.get('DATABASE_PRIVATE_URL') or
        os.environ.get('PGURL')
    )
    
    # Or construct from individual components if available
    if not database_url and all([
        os.environ.get('PGHOST'),
        os.environ.get('PGUSER'),
        os.environ.get('PGPASSWORD'),
        os.environ.get('PGDATABASE')
    ]):
        pghost = os.environ.get('PGHOST')
        pguser = os.environ.get('PGUSER')
        pgpassword = os.environ.get('PGPASSWORD')
        pgdatabase = os.environ.get('PGDATABASE')
        pgport = os.environ.get('PGPORT', '5432')
        database_url = f"postgresql://{pguser}:{pgpassword}@{pghost}:{pgport}/{pgdatabase}"
        print(f"DEBUG: Constructed DATABASE_URL from PG* variables")
    
    print(f"DEBUG: DATABASE_URL exists: {database_url is not None}")
    print(f"DEBUG: DATABASE_URL value: {database_url[:50] if database_url else 'None'}...")
    
    if database_url:
        DATABASES = {
            'default': dj_database_url.config(
                default=database_url,
                conn_max_age=600,
                conn_health_checks=True,
            )
        }
        print(f"DEBUG: Using PostgreSQL database")
    else:
        # Fallback to SQLite if DATABASE_URL not set
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
        print(f"DEBUG: Falling back to SQLite")
    
    # Static files with WhiteNoise
    if 'whitenoise.middleware.WhiteNoiseMiddleware' not in MIDDLEWARE:
        MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
    # Simplified static files storage
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
    WHITENOISE_USE_FINDERS = True
    
    # Security settings
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    # Temporarily disabled for debugging
    # SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    
    # Use environment variable for SECRET_KEY in production
    SECRET_KEY = os.environ.get('SECRET_KEY', SECRET_KEY)

