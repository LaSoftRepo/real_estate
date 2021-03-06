import json
import os
from django.contrib.messages import constants as messages

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INSTALLED_APPS = [
    'dal',
    'dal_select2',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.redirects',

    # origin
    'ckeditor',
    'ckeditor_uploader',
    'easy_thumbnails',
    'solo',
    'django_filters',
    'multiselectfield',

    # own
    'users',
    'admin2',
    'common',
    'articles',
    'services',
    'rieltor_object',
    'trust',
    'contact',
    'videos',
    'favorites',
    'plan',
    'polls',
    'banners',
    'seo',
    'landing',
    'privat24',
    'liqpayapp',
    'landingpage',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'common.middleware.RedirectMiddlewareCustom',
]

ROOT_URLCONF = 'gek.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'common.context_processors.counter',
            ],
        },
    },
]

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

SITE_ID = 1

WSGI_APPLICATION = 'gek.wsgi.application'

AUTH_USER_MODEL = 'users.User'

LOGIN_REDIRECT_URL = '/admin/'
LOGIN_URL = '/admin/login/'
LOGOUT_URL = '/admin/login/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_IMAGE_BACKEND = 'pillow'

CKEDITOR_UPLOAD_SLUGIFY_FILENAME = True

CKEDITOR_CONFIGS = {
    'default': {
        'contentsCss': '/static/ckeditor/ckeditor/custom_fonts/fonts.css',
        'font_names': 'PFDinTextCompPro/PFDinTextCompPro; Roboto/Roboto',
        'skin': 'moono-lisa',
        'fontSize_sizes': '14/14px;16/16px;20/20px;24/24px;',
        # 'skin': 'office2013',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', '-', 'Undo', 'Redo']},
            {'name': 'tools', 'items': ['Maximize', 'Preview','ShowBlocks']},
            # {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            # {'name': 'forms',
            #  'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
            #            'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            # {'name': 'insert',
             # 'items': ['Image', 'Update','Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            # '/',
            {'name': 'styles', 'items': ['Font', 'FontSize']},
            # {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            '/',

            # {'name': 'about', 'items': ['About']},
              # put this to force next toolbar on new line
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 840,
        'toolbarCanCollapse': False,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join(
            [
                # your extra plugins here
                'div',
                'autolink',
                'autoembed',
                'embedsemantic',
                'autogrow',
                # 'devtools',
                'widget',
                'lineutils',
                'clipboard',
                'dialog',
                'dialogui',
                'elementspath'
            ]),
    }
}

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

FILE_UPLOAD_MAX_MEMORY_SIZE = 2621440

THUMBNAIL_ALIASES = {
    '': {
        'infrastructure_image_40': {'size': (40, 40), 'crop': True},
        'article_image_60': {'size': (60, 60), 'crop': True},
        'article_image_80_40': {'size': (80, 40), 'crop': True},
        'admin_avatar_200': {'size': (200, 200), 'crop': True},
        'gallery_image_233': {'size': (233, 133), 'crop': True},
        'gallery_image_275': {'size': (275, 185), 'crop': True},
        'gallery_image_370': {'size': (370, 211), 'crop': True},
        'gallery_image_570': {'size': (570, 338), 'crop': True},
        'newbuild_index_image_570': {'size': (570, 269), 'crop': True},
        'gallery_image_469': {'size': (469, 266), 'crop': True},
        'universal_image_270': {'size': (270, 160), 'crop': True},
        'slider_image_166': {'size': (166, 94), 'crop': True},
        'earth_image_542': {'size': (542, 293), 'crop': True},
        'trust_image_344': {'size': (344, 245), 'crop': True},
        'trust_image_372': {'size': (372, 212), 'crop': True},
        'user_avatar_270_330': {'size': (270, 330), 'crop': True},
        'test_427': {'size': (427, 245), 'crop': True},
        'seo_480': {'size': (480, 287), 'crop': True},
        'article_271': {'size': (271, 154), 'crop': True},
        'service_585': {'size': (585, 248), 'crop': True},
        'service_370': {'size': (370, 154), 'crop': True},
        'slider_1110': {'size': (1110, 624), 'crop': 'zoom'},
    },
}

with open('media_path.json', 'w') as f:
    f.write(json.dumps({'path': MEDIA_ROOT}))
