from .base import *
import dj_database_url

ENVIRONMENT = 'production'
DEBUG = True
ALLOWED_HOSTS = ['*']
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
# DATABASES['default'] = dj_database_url.config(
#     default=''
# )
