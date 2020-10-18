import sys

try:
    from django.conf import settings

    settings.configure(
        DEBUG=True,
        LANGUAGE_CODE='en-us',
        USE_TZ=True,
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'djangocms_youtube',
            }
        },
        ROOT_URLCONF='djangocms_youtube.urls',
        INSTALLED_APPS=[
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sites',
            'cms',
            'menus',
            'djangocms_youtube',
            'easy_thumbnails',
            'treebeard',
            'filer',
        ],
        SITE_ID=1,
        NOSE_ARGS=['-s'],
        TEMPLATES=[
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'OPTIONS': {
                    'context_processors': [
                        'django.template.context_processors.request',
                        'cms.context_processors.cms_settings',
                    ],

                },
            },
        ]
    )

    try:
        import django
        setup = django.setup
    except AttributeError:
        pass
    else:
        setup()

    from django_nose import NoseTestSuiteRunner
except ImportError:
    import traceback
    traceback.print_exc()
    raise ImportError('To fix this error, run: pip install -r requirements-test.txt')


def run_tests(*test_args):
    if not test_args:
        test_args = ['tests']

    # Run tests
    test_runner = NoseTestSuiteRunner(verbosity=1)

    failures = test_runner.run_tests(test_args)

    if failures:
        sys.exit(failures)


if __name__ == '__main__':
    run_tests(*sys.argv[1:])
