# -*- coding: utf-8 -*-
SECRET_KEY = "b'fqrsy_!g)#9tx^b+v)$6@_7j9_r3zdy_s))nf^sqathw9bgeca'"
SERVICE_URL = "http://172.22.0.20/"
ALLOWED_HOSTS = ['seafile.local.com','.localhost','172.22.0.20' ,'127.0.0.1', '[::1]']
ENABLE_WIKI = True
USE_PDFJS = True
FILE_PREVIEW_MAX_SIZE = 300 * 1024 * 1024

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'seahub_db',
        'USER': 'seafile',
        'PASSWORD': 'cf3a294a-f23d-4e73-ad3c-f5ff082cffa6',
        'HOST': 'db',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}


CACHES = {
    'default': {
        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
        'LOCATION': 'memcached:11211',
    },
    'locmem': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
}
COMPRESS_CACHE_BACKEND = 'locmem'
TIME_ZONE = 'Etc/UTC'
FILE_SERVER_ROOT = "http://172.22.0.20/seafhttp"

