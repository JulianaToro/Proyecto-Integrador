# Conexión a DB RegistrosDataYa
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.dummy',
    },

    'accounts_db': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'accounts_db',
        'USER': 'root',
        'PASSWORD': 'Sajina01*',
        'HOST': '127.0.0.1',
        'PORT': '',
    },

    'analitycs_db': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'analytics_db',
        'USER': 'root',
        'PASSWORD': 'Sajina01*',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

# Modelo de autenticación
AUTH_USER_MODEL = 'DataYaProject.CustomUser'

# Enrutador de las bases de datos
DATABASE_ROUTERS = ['path.to.AppRouter']