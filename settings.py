import os
from os import environ

import dj_database_url

import otree.settings


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# the environment variable OTREE_PRODUCTION controls whether Django runs in
# DEBUG mode. If OTREE_PRODUCTION==1, then DEBUG=False
if environ.get('OTREE_PRODUCTION') not in {None, '', '0'}:
    DEBUG = False
else:
    DEBUG = True

# don't share this with anybody.
SECRET_KEY = ''


DATABASES = {
    'default': dj_database_url.config(
        # Rather than hardcoding the DB parameters here,
        # it's recommended to set the DATABASE_URL environment variable.
        # This will allow you to use SQLite locally, and postgres/mysql
        # on the server
        # Examples:
        # export DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
        # export DATABASE_URL=mysql://USER:PASSWORD@HOST:PORT/NAME

        # fall back to SQLite if the DATABASE_URL env var is missing
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    )
}

# AUTH_LEVEL:
# this setting controls which parts of your site are freely accessible,
# and which are password protected:
# - If it's not set (the default), then the whole site is freely accessible.
# - If you are launching a study and want visitors to only be able to
#   play your app if you provided them with a start link, set it to STUDY.
# - If you would like to put your site online in public demo mode where
#   anybody can play a demo version of your game, but not access the rest
#   of the admin interface, set it to DEMO.

# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')


# setting for integration with AWS Mturk
AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')


# e.g. EUR, CAD, GBP, CHF, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True
POINTS_DECIMAL_PLACES = 3
REAL_WORLD_CURRENCY_DECIMAL_PLACES = 2

SENTRY_DSN = environ.get('SENTRY_DSN')

# e.g. en, de, fr, it, ja, zh-hans
# see: https://docs.djangoproject.com/en/1.9/topics/i18n/#term-language-code
LANGUAGE_CODE = 'en'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

# SENTRY_DSN = ''

DEMO_PAGE_INTRO_HTML = """
<ul>
    <li>
        <a href="https://github.com/oTree-org/otree" target="_blank">
            oTree on GitHub
        </a>.
    </li>
    <li>
        <a href="http://www.otree.org/" target="_blank">
            oTree homepage
        </a>.
    </li>
</ul>
<p>
    Here are various games implemented with oTree. These games are all open
    source, and you can modify them as you wish.
</p>
"""

ROOMS = [
    {
        'name': 'lab',
        'display_name': 'VSEEL (KRAN 701)',
        'participant_label_file': '_rooms/VSEEL701.txt',
    },
]


mturk_hit_settings = {
    'keywords': ['bonus', 'study'],
    'title': 'Title for your experiment',
    'description': 'Description for your experiment',
    'frame_height': 500,
    'preview_template': 'global/MTurkPreview.html',
    'minutes_allotted_per_assignment': 60,
    'expiration_hours': 7*24, # 7 days
    #'grant_qualification_id': 'YOUR_QUALIFICATION_ID_HERE',# to prevent retakes
    'qualification_requirements': []
}


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 0.005,
    'participation_fee': 5.00,
    'doc': "",
    'mturk_hit_settings': mturk_hit_settings,
}

SESSION_CONFIGS = [


    {
        'name': 'SCP_Session25',
        'display_name': "01-28-2018 2.30pm -- Session 25 (R=48,S=9)",
        'num_demo_participants': 2,
        'app_sequence': [
            'SCP00_Consent',
            'SCP01_Introduction',
            'SCP02_Personality',
            'SCP03_IQ',
            'SCP04_PayoffsInstructions',
            'SCP05_TestingInstructions',
            'SCP06_Experiment',
            'SCP08_PayoffScreen',
            'SCP07_Demographics'],

        'R': 48,
        'Sequence': 9,
        'doc': """
        Edit the 'R' parameter to change the payoff to mutual cooperation.
        Edit the 'Sequence' parameter to change which sequence of supergame lengths is used.
    """

    },

    {
        'name': 'SCP_Session26',
        'display_name': "01-28-2018 4.00pm -- Session 26 (R=32,S=9)",
        'num_demo_participants': 2,
        'app_sequence': [
            'SCP00_Consent',
            'SCP01_Introduction',
            'SCP02_Personality',
            'SCP03_IQ',
            'SCP04_PayoffsInstructions',
            'SCP05_TestingInstructions',
            'SCP06_Experiment',
            'SCP08_PayoffScreen',
            'SCP07_Demographics'],

        'R': 32,
        'Sequence': 9,
        'doc': """
    Edit the 'R' parameter to change the payoff to mutual cooperation.
    Edit the 'Sequence' parameter to change which sequence of supergame lengths is used.
"""

    },

    {
        'name': 'SCP_Session27',
        'display_name': "01-28-2018 5.30pm -- Session 27 (R=40,S=9)",
        'num_demo_participants': 2,
        'app_sequence': [
            'SCP00_Consent',
            'SCP01_Introduction',
            'SCP02_Personality',
            'SCP03_IQ',
            'SCP04_PayoffsInstructions',
            'SCP05_TestingInstructions',
            'SCP06_Experiment',
            'SCP08_PayoffScreen',
            'SCP07_Demographics'],

        'R': 40,
        'Sequence': 9,
        'doc': """
    Edit the 'R' parameter to change the payoff to mutual cooperation.
    Edit the 'Sequence' parameter to change which sequence of supergame lengths is used.
"""

    },
]

#install dj_database_url

# anything you put after the below line will override
# oTree's default settings. Use with caution.
# otree.settings.augment_settings(globals())
