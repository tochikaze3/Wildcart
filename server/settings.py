"""
Django settings for server project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""



import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3^@pqc@i8o-33qiv13*h(873xljml^3d9r1nkmvkqv!rnm!_z%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['wildcart.herokuapp.com', '0.0.0.0', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    #'accounts',
    'social_django',
    'api',
    'stores',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'corsheaders',
    'allauth', 
    'allauth.account', 
    'allauth.socialaccount',
    'rest_auth.registration',
]

#AUTH_USER_MODEL='accounts.Account'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

# CORS CONFIGURATION
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST= ('http://localhost:5000', 'http://localhost:3000', 'http://localhost:5555',)


ROOT_URLCONF = 'server.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',  
                'social_django.context_processors.login_redirect', 
            ],
        },
    },
]

WSGI_APPLICATION = 'server.wsgi.application'


#AUTHENTICATION_BACKENDS = (  
 # 'drf_social_oauth2.backends.DjangoOAuth2',
  #'django.contrib.auth.backends.ModelBackend',)
#REST_FRAMEWORK = {
 #  'DEFAULT_AUTHENTICATION_CLASSES': (
  #     'oauth2_provider.contrib.rest_framework.OAuth2Authentication',  
   #    'drf_social_oauth2.authentication.SocialAuthentication',
   #)
#}

#REST_AUTH_SERIALIZERS = {
  #  'USER_DETAILS_SERIALIZER': 'api.serializers.UserSerializer',
#}


#REST FRAMEWORK CONFIGURATION

<<<<<<< HEAD
#REST_FRAMEWORK = { 
 #   'DEFAULT_PERMISSION_CLASSES': [
  #  'rest_framework.permissions.IsAuthenticated',],
  #  'DEFAULT_AUTHENTICATION_CLASSES': [ 
   # 'rest_framework.authentication.SessionAuthentication', 
    #'rest_framework.authentication.BasicAuthentication',
    #'oauth2_provider.contrib.rest_framework.OAuth2Authentication',  
    #'drf_social_oauth2.authentication.SocialAuthentication',], }
=======
REST_FRAMEWORK = { 
    'DEFAULT_PERMISSION_CLASSES': [
    'rest_framework.permissions.IsAuthenticated',
],
    'DEFAULT_AUTHENTICATION_CLASSES': [ 
    'rest_framework.authentication.SessionAuthentication', 
    'rest_framework.authentication.BasicAuthentication',
],

'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
    }
>>>>>>> test
    

ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False

AUTHENTICATION_BACKENDS = (

    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' 


SITE_ID = 1 



# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd7120nmt72g8ok',
        'HOST': 'ec2-54-87-112-29.compute-1.amazonaws.com',
        'PORT': 5432,
        'USER': 'dbyolnhegemfyg',
        'PASSWORD': '1f6261e67caa0ce7a5a889d81199a80929ba26fdd63e09bf88859e652767aa5f'
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/staticfiles/'
#STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
