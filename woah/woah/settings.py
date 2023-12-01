import environ
import os

# Development or Production?
IN_PRODUCTION = False

# Get URLS
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_DIR = os.path.join(BASE_DIR, "woah/envs")
if IN_PRODUCTION:
    ENV_FILE = os.path.join(ENV_DIR, ".env.prod")
else: 
    ENV_FILE = os.path.join(ENV_DIR, ".env.dev")

# Load the environment
env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env(ENV_FILE)

# Import environment variables
DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

INSTALLED_APPS = [
    # This project
    "website",
    "custom_media",
    "custom_user",
    # Wagtail CRX (CodeRed Extensions)
    "coderedcms",
    "django_bootstrap5",
    "modelcluster",
    "taggit",
    "wagtailcache",
    "wagtailseo",
    # Wagtail
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail",
    "wagtail.contrib.settings",
    "wagtail.contrib.table_block",
    "wagtail.admin",
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    'django_plotly_dash.apps.DjangoPlotlyDashConfig',
    "django_sass",
    # Other
    'channels', # for live plotly dashboards
]

MIDDLEWARE = [
    # Save pages to cache. Must be FIRST.
    "wagtailcache.cache.UpdateCacheMiddleware",
    # Common functionality
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.common.CommonMiddleware",
    # Security
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    # Plotly
    "django_plotly_dash.middleware.BaseMiddleware",
    "django_plotly_dash.middleware.ExternalRedirectionMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # CMS functionality
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
    # Fetch from cache. Must be LAST.
    "wagtailcache.cache.FetchFromCacheMiddleware",
]

ROOT_URLCONF = "woah.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "wagtail.contrib.settings.context_processors.settings",
            ],
        },
    },
]

WSGI_APPLICATION = "woah.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    # default
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sl3")
    },
}
'''
# Can't use postgres 9 with django 4. Gives this error:
# django.db.utils.ProgrammingError: column c.relispartition does not exist
DATABASES = {
    # default
    "default": {
        "ENGINE": env("WOAH_DB_ENGINE"),
        'NAME': env("WOAH_DB_NAME"),
        'USER': env("WOAH_DB_USERNAME"),
        'PASSWORD': env("WOAH_DB_PASSWORD"),
        'HOST': env("WOAH_DB_HOST"),
    },
}
'''

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "custom_user.User"

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "America/New_York"
USE_I18N = False
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATICFILES_FINDERS = [
    # default
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    # plotly
    'django_plotly_dash.finders.DashAssetFinder',
    'django_plotly_dash.finders.DashComponentFinder',
    'django_plotly_dash.finders.DashAppDirectoryFinder',
]

STATIC_ROOT = os.path.join(BASE_DIR, "website/static")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "website/media")
MEDIA_URL = "/media/"

# Email
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
SERVER_EMAIL = env("SERVER_EMAIL")
SERVER_PORT = env("SERVER_PORT")

DEFAULT_FROM_EMAIL = "WOAH <info@localhost>"
# A list of all the people who get code error notifications.
if IN_PRODUCTION:
    ADMINS = [
        ("GBO SDD", "gbosdd@nrao.edu"),
    ]
else:
    ADMINS = [
        ("Victoria Catlett", "vcatlett@nrao.edu"),
    ]
MANAGERS = ADMINS
# A list of all the people who should get broken link notifications.
SERVER_EMAIL = DEFAULT_FROM_EMAIL

# Login

LOGIN_URL = "wagtailadmin_login"
LOGIN_REDIRECT_URL = "wagtailadmin_home"


# Wagtail settings

WAGTAIL_SITE_NAME = "WOAH"
WAGTAIL_ENABLE_UPDATE_CHECK = False
WAGTAILIMAGES_IMAGE_MODEL = "custom_media.CustomImage"
WAGTAILDOCS_DOCUMENT_MODEL = "custom_media.CustomDocument"

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
WAGTAILADMIN_BASE_URL = "http://localhost"

if IN_PRODUCTION:
    WAGTAIL_CACHE = True
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
            "LOCATION": os.path.join(BASE_DIR, "cache"),
            "KEY_PREFIX": "coderedcms",
            "TIMEOUT": 14400,
        }
    }
else:
    WAGTAIL_CACHE = False

# Tags

TAGGIT_CASE_INSENSITIVE = True


# Sets default for primary key IDs
# See https://docs.djangoproject.com/en/4.2/ref/models/fields/#bigautofield
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Plotly Settings
X_FRAME_OPTIONS = 'SAMEORIGIN'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [('127.0.0.1', 6379),],
        },
    },
}

PLOTLY_DASH = {
    # Route used for the message pipe websocket connection
    "ws_route" :   "dpd/ws/channel",
    # Route used for direct http insertion of pipe messages
    "http_route" : "dpd/views",
    # Flag controlling existince of http poke endpoint
    "http_poke_enabled" : True,
    # Insert data for the demo when migrating
    "insert_demo_migrations" : False,
    # Timeout for caching of initial arguments in seconds
    "cache_timeout_initial_arguments": 60,
    # Name of view wrapping function
    "view_decorator": None, # "django_plotly_dash.access.login_required"
    # Flag to control location of initial argument storage
    "cache_arguments": True,
    # Flag controlling local serving of assets
    "serve_locally": False,
}

PLOTLY_COMPONENTS = [
    'dpd_components',
    'dpd_static_support',
    'dash_bootstrap_components',
]