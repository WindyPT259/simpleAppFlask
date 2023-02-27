

# Connect DB
SQLALCHEMY_DATABASE_URI = 'mysql +pymysql://root:250997@localhost/sampleapp?charset=utf8mb4'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_POOL_TIMEOUT = 20

DEBUG = True

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Auto reload templates
TEMPLATES_AUTO_RELOAD = True

# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"
