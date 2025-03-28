ALLOWED_HOSTS = ['*']
SITE_URL = ""

SECRET_KEY = "J_cQPuPEK05kO@BTwjDSnQ&drj3z+H80$@3bDj()+!PQKidSNz"

DATABASE = {
    'NAME': 'statuspage',          # Database name
    'USER': 'statuspage',          # PostgreSQL username
    'PASSWORD': 'abcdefgh123456',   # PostgreSQL password
    'HOST': 'db',            # Database server
    'PORT': '',                     # Database port (leave blank for default)
    'CONN_MAX_AGE': 300,            # Max database connection age (seconds)
}

REDIS = {
    'tasks': {
        'HOST': 'redis',      # Redis server
        'PORT': 6379,             # Redis port
        'PASSWORD': '',           # Redis password (optional)
        'DATABASE': 0,            # Database ID
        'SSL': False,             # Use SSL (optional)
    },
    'caching': {
        'HOST': 'redis',
        'PORT': 6379,
        'PASSWORD': '',
        'DATABASE': 1,            # Unique ID for second database
        'SSL': False,
    }
}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DATABASE['NAME'],
        'USER': DATABASE['USER'],
        'PASSWORD': DATABASE['PASSWORD'],
        'HOST': DATABASE['HOST'],
        'PORT': DATABASE['PORT'] or '5432',
        'CONN_MAX_AGE': DATABASE.get('CONN_MAX_AGE', 0),
    }
}
