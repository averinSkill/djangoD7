"""
Django settings for NewsPortal project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-th(x%tr_6_m_16&oy+bm6rgrx&^fn1lox(as48wp=1aihp50vh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # подключаем ещё приложения
    'django.contrib.sites',
    'django.contrib.flatpages',
    'fpages',
    # 'news',
    'news.apps.NewsConfig',
    'django_filters',

    'sign',
    'protect',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth.account.forms',
    # ... include the providers you want to enable:
    'allauth.socialaccount.providers.google',
    # D6
    'appointments',
    # D6.5
    'django_apscheduler',
]

SITE_ID = 1

DEFAULT_FROM_EMAIL = 'apractikant@yandex.ru'

LOGIN_URL = '/accounts/login/'
# При корректных данных для входа, пользователь перенаправляется на страницу, указанною по данному пути
# страница, куда перенаправляется пользователь после успешного входа на сайт, в данном случае корневая страница сайта
LOGIN_REDIRECT_URL = '/news/'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'NewsPortal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), os.path.join(BASE_DIR, 'appointments\\templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # `allauth` needs this from django
                'django.template.context_processors.request',
            ],
        },
    },
]


ACCOUNT_FORMS = {'signup': 'sign.models.BasicSignupForm'}

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'



AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]



WSGI_APPLICATION = 'NewsPortal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

# D6
EMAIL_HOST = 'smtp.yandex.ru'  # адрес сервера Яндекс-почты для всех один и тот же
EMAIL_PORT = 465  # порт smtp сервера тоже одинаковый
EMAIL_HOST_USER = 'apractikant'  # ваше имя пользователя, например, если ваша почта user@yandex.ru, то сюда надо писать user, иными словами, это всё то что идёт до собаки
EMAIL_HOST_PASSWORD = ''  # пароль от почты
EMAIL_USE_SSL = True  # Яндекс использует ssl, подробнее о том, что это, почитайте в дополнительных источниках, но включать его здесь обязательно

# D6.5
# формат даты, которую будет воспринимать наш задачник (вспоминаем модуль по фильтрам)
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
# если задача не выполняется за 25 секунд, то она автоматически снимается, можете поставить время побольше, но как правило, это сильно бьёт по производительности сервера
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Seconds


# D7
CELERY_BROKER_URL = 'redis://:qjUWGrrkcYhAJfqQrrPr8eltT0q2i1vn@redis-13191.c1.asia-northeast1-1.gce.cloud.redislabs.com:13191'
CELERY_RESULT_BACKEND = 'redis://:qjUWGrrkcYhAJfqQrrPr8eltT0q2i1vn@redis-13191.c1.asia-northeast1-1.gce.cloud.redislabs.com:13191'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

if DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


LOGGING = {
    'version': 1,
    'disable_existing_logger': False,
    'loggers': {
        'django': {
            'handlers': ['console', 'console_warning', 'console_err_crit', 'general'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['errorlog', 'mail_admins'],
            'level': 'CRITICAL',
            'propagate': False,
        },
        'django.server': {
            'handlers': ['errorlog', 'mail_admins'],
            'level': 'CRITICAL',
            'propagate': False,
        },
        'django.template': {
            'handlers': ['errorlog'],
            'level': 'ERROR',
        },
        'django.db_backends': {
            'handlers': ['errorlog'],
            'level': 'ERROR',
        },
        'django.security': {
            'handlers': ['securitylog'],
            'level': 'ERROR',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'console',
            'filters': ['require_debug_true'],
        },
        'console_warning': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'console_warning',
            'filters': ['require_debug_true'],
        },
        'console_err_crit': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'err_crit',
            'filters': ['require_debug_true'],
        },
        'general': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'general.log',
            'formatter': 'general',
            'filters': ['require_debug_false'],
        },
        'errorlog': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'error.log',
            'formatter': 'err_crit',
        },
        'securitylog': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'security.log',
            'formatter': 'general',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
        },
    },
    'formatters': {
        'console': {
            'format': '{asctime} {levelname} {message}',
            'datetime': '%Y.%m.%d %H:%M:%S',
            'style': '{',
        },
        'console_warning': {
            'format': '{asctime} {levelname} {message} {pathname}',
            'datetime': '%Y.%m.%d %H:%M:%S',
            'style': '{',
        },
        'err_crit': {
            'format': '{asctime} {levelname} {message} {pathname} {exc_info}',
            'datetime': '%Y.%m.%d %H:%M:%S',
            'style': '{',
        },
        'general': {
            'format': '{asctime} {levelname} {module} {message}',
            'datetime': '%Y.%m.%d %H:%M:%S',
            'style': '{',
        }
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    }
}

