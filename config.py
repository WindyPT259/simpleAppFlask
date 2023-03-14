# APIURL
API_URL = "http://127.0.0.1:5000"
# Connect DB
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:250997@localhost/sampleapp?charset=utf8mb4'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_POOL_TIMEOUT = 20

DEBUG = True

# Celery configuration
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_INCLUDE = ['tasks']


# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Auto reload templates
TEMPLATES_AUTO_RELOAD = True

# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"
