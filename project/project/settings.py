"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 3.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
# from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = config('SECRET_KEY')
SECRET_KEY = 'django-insecure-=-+&#q=58ma35-nr*%n^bxc(sqe^z9@@_p=u#8p(nl6@n16clt'

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
    'blog',
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

ROOT_URLCONF = 'project.urls'

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

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
# STOCK01_POSTGRES_NAME = os.environ.get("POSTGRES_PORT")
# STOCK01_POSTGRES_USER = os.environ.get()
# STOCK01_POSTGRES_PASSWORD = Rlarn881259!
# STOCK01_POSTGRES_HOST = 127.0.0.1
# STOCK01_POSTGRES_PORT = 5432

DATABASES = {
    'db_stock01': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_stock01',
        'USER': 'stock_user',
        'PASSWORD': 'Rlarn881259!',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        # 'NAME': config('STOCK01_POSTGRES_NAME'),
        # 'USER': config('STOCK01_POSTGRES_USER'),
        # 'PASSWORD': config('STOCK01_POSTGRES_PASSWORD'),
        # 'HOST': config('STOCK01_POSTGRES_HOST'),
        # 'PORT': config('STOCK01_POSTGRES_PORT'),
    },
    'db_stock02': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_stock02',
        'USER': 'stock_user',
        'PASSWORD': 'Rlarn881259!',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        # 'NAME': config('STOCK02_POSTGRES_NAME'),
        # 'USER': config('STOCK02_POSTGRES_USER'),
        # 'PASSWORD': config('STOCK02_POSTGRES_PASSWORD'),
        # 'HOST': config('STOCK02_POSTGRES_HOST'),
        # 'PORT': config('STOCK02_POSTGRES_PORT'),
    },
    'db_stock03': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_stock03',
        'USER': 'stock_user',
        'PASSWORD': 'Rlarn881259!',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        # 'NAME': config('STOCK03_POSTGRES_NAME'),
        # 'USER': config('STOCK03_POSTGRES_USER'),
        # 'PASSWORD': config('STOCK03_POSTGRES_PASSWORD'),
        # 'HOST': config('STOCK03_POSTGRES_HOST'),
        # 'PORT': config('STOCK03_POSTGRES_PORT'),
    },
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_stock01',
        'USER': 'stock_user',
        'PASSWORD': 'Rlarn881259!',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        # 'NAME': config('STOCK01_POSTGRES_NAME'),
        # 'USER': config('STOCK01_POSTGRES_USER'),
        # 'PASSWORD': config('STOCK01_POSTGRES_PASSWORD'),
        # 'HOST': config('STOCK01_POSTGRES_HOST'),
        # 'PORT': config('STOCK01_POSTGRES_PORT'),
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
}
# PostgreSQL: django.db.backends.postgresql

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

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

# os 라이브러리 사용하기 위해 가져오기
import os

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
