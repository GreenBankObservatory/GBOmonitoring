# General imports
import os
from email.utils import getaddresses
from getpass import getuser
from pathlib import Path

# Django imports
from django.core.management.commands.runserver import Command as rs
import django_stubs_ext
import environ
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

django_stubs_ext.monkeypatch()

_user = getuser()
env = environ.Env(
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, []),
    INTERNAL_IPS=(list, []),
    IPYTHON_ARGUMENTS=(list, []),
    SERVER_PORT=(int, None),
    ALLOWED_USERNAMES=(list, []),
    SENTRY_ENV=(str, f"{_user}_dev"),
    ADS_DEV_KEY=(str, None),
)
# Allow overriding of env file path via ENV_PATH
environ.Env.read_env(env.str("ENV_PATH", "astro_site/.env"))


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DEBUG = env("DEBUG")
SERVER_EMAIL = env("SERVER_EMAIL")
EMAIL_HOST = env("EMAIL_HOST")

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env("ALLOWED_HOSTS")
SERVER_PORT = env("SERVER_PORT")
APPEND_SLASH = True
DEFAULT_FROM_EMAIL = "noreply@gb.nrao.edu"
rs.default_port = SERVER_PORT

# Application definition

INSTALLED_APPS = [
    "dal",
    "dal_select2",
    "django.contrib.sites",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
    "django_celery_results",
    "django_cas_ng",
    "pgtrigger",
    "django_require_login",
    "watson",
    "debug_toolbar",
    "django_extensions",
    "django_tables2",
    "django_filters",
    "crispy_forms",
    "crispy_bootstrap4",
    "alert",
    "util",
    "prometheus",
    "visualization",
]

# https://docs.djangoproject.com/en/3.1/topics/cache/#order-of-middleware
MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django_cas_ng.middleware.CASMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "watson.middleware.SearchContextMiddleware",
    "django_require_login.middleware.LoginRequiredMiddleware",
]

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "django_cas_ng.backends.CASBackend",
)

ROOT_URLCONF = "woah.urls"

TEMPLATE_DIR = os.path.join(BASE_DIR, 'woah/templates')
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [TEMPLATE_DIR],
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
        },
    }
]

WSGI_APPLICATION = "woah.wsgi.application"


# Database

DATABASES = {
    "default": {
        **env.db("WOAH_DB_URL"),
        "CONN_MAX_AGE": 3600,
        "TEST": {"DEPENDENCIES": []},
    },
}
DATABASE_ROUTERS = ["dynamic_db_router.DynamicDbRouter"]

# For nell to be able to query PST
# PST = env.db("PST_DB_URL")

# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization

LANGUAGE_CODE = "en-us"
# TIME_ZONE = "America/New_York"
TIME_ZONE = "UTC"
USE_I18N = False
USE_L10N = False
USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "woah/static")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "woah/staticfiles"),
]
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
]

# django-tables2
# Use Bootstrap4 table classes
DJANGO_TABLES2_TEMPLATE = "django_tables2/bootstrap4.html"


# django-crispy-forms
# Use Bootstrap4 form classes
CRISPY_TEMPLATE_PACK = "bootstrap4"

# For debug toolbar
INTERNAL_IPS = env("INTERNAL_IPS")

# Additional imports whenever running ./manage.py shell_plus
SHELL_PLUS_POST_IMPORTS = [
    ["tqdm", ["tqdm"]],
    ["django.conf", ["settings"]],
    ["util.tools.benchmark", ["Benchmark"]],
    ["rich", ["inspect"]],
]

# Namespace model name conflicts
SHELL_PLUS_MODEL_IMPORTS_RESOLVER = "util.tools.collision_resolvers.SensibleCR"
IPYTHON_ARGUMENTS = env("IPYTHON_ARGUMENTS")

# logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {"format": "%(levelname)s %(asctime)s %(message)s"},
        "fancy": {"format": "%(asctime)s - %(levelname)s - %(funcName)s - %(message)s"},
        "unittest": {"format": "%(levelname)s - %(module)s.%(funcName)s - %(message)s"},
    },
    "handlers": {
        "log_to_stdout": {
            "level": "DEBUG",
            "class": "util.tools.handlers.TqdmLoggingHandler",
            "formatter": "simple",
        },
        "log_to_stdout_verbose": {
            "level": "DEBUG",
            "class": "util.tools.handlers.TqdmLoggingHandler",
            "formatter": "fancy",
        },
    },
    "loggers": {
        "woah": {
            "handlers": ["log_to_stdout"],
            "level": "INFO",
            "propagate": True,
        },
        "django.db.backends": {
            "handlers": ["log_to_stdout"],
            "level": "WARNING",
            "propagate": True,
        },
        "collatelogs": {
            "handlers": ["log_to_stdout"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}

# Needed because nell is dumb
USE_REVERSION = False
DATETIME_FORMAT = "Y-m-j H:i:s"
SHORT_DATETIME_FORMAT = "Y-m-j H:i:s"
EMAIL_SUBJECT_PREFIX = "[WOAH] "
SITE_ID = 1
LOGIN_REDIRECT_URL = "/"

# django_cas_ng
CAS_SERVER_URL = "https://my.nrao.edu/cas/login"
CAS_LOGOUT_URL = "https://my.nrao.edu/cas/logout"
CAS_ADMIN_PREFIX = "admin"
CAS_APPLY_ATTRIBUTES_TO_USER = True

ALLOWED_USERNAMES = env("ALLOWED_USERNAMES")

def check_allowlist(user):
    from django.core.exceptions import PermissionDenied

    if user.is_authenticated:
        if user.username in ALLOWED_USERNAMES:
            # If user is authenticated AND allow-listed, they have full access
            return True
        else:
            # If user is authenticated, but NOT allow-listed, raise a 403
            print(f"User {user.username} is authenticated but NOT allow-listed!")
            raise PermissionDenied()

    return False


# REQUIRE_LOGIN_NAMED_PUBLIC_URLS = ("cas_ng_login", "cas_ng_logout")
REQUIRE_LOGIN_PUBLIC_URLS = ("^/accounts/login/?.*", "^/admin/?.*")
REQUIRE_LOGIN_USER_TEST_FUNC = check_allowlist
ADMINS = getaddresses([env("DJANGO_ADMINS")])

CACHES = {
    "default": env.cache(),
}
CACHE_MIDDLEWARE_SECONDS = 0

if "SENTRY_DSN" in os.environ:
    sentry_sdk.init(
        environment=env("SENTRY_ENV"),
        integrations=[DjangoIntegration()],
        traces_sample_rate=1.0,
        send_default_pii=True,
    )

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


CELERY_RESULT_BACKEND = "django-db"
CELERY_BROKER_URL = env("CELERY_BROKER_URL")
CELERY_RESULT_EXTENDED = True  # needed for tracebacks, etc. to get saved

DEFAULT_EXPORT_PATH = env("DEFAULT_EXPORT_PATH")

FILE_UPLOAD_PERMISSIONS = 0o644
FILE_UPLOAD_DIRECTORY_PERMISSIONS = 0o755