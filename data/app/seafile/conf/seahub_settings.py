# -*- coding: utf-8 -*-
SECRET_KEY = "b'lc=7+&o4+rm%h9!dc0ld#l=*@8#fxq7ri)!#@y-3m-^a-b8$%g'"
SERVICE_URL = "http://172.22.0.20/"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'seahub_db',
        'USER': 'seafile',
        'PASSWORD': 'e8069d8a-f3ea-449e-a903-5468b20842b5',
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
