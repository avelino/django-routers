# django-routers

Django multiple databases, auto routers


# Install

    pip install django-routers


# Usage

Add in settings:

    DATABASE_ROUTERS = ['routers.router.AutoRouter']


## Settings example:

* Written by **default**
* Reading by **default** and **slave**


    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'routers',
            'USER': 'root',
            'PASSWORD': 'root',
            'HOST': '127.0.0.1',
        },
        'slave': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'routers_more',
            'USER': 'root',
            'PASSWORD': 'root',
            'HOST': '10.0.0.2',
        }
    }

    DATABASE_ROUTERS = ['routers.router.AutoRouter']


## Advanced options

Settings Variables

* ROUTERS_READ
** Declares which server is reading
* ROUTERS_WRITE
** Declares which server is written
* ROUTERS_ALLOW_RELATION
** Declares whether we consulted on more than one database, default is **True**