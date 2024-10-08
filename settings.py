from os import environ


SESSION_CONFIGS = [

    dict(
        name='game',
        display_name="Game",
        num_demo_participants=2,  # 总人数
        app_sequence=['dictator_game','dictator_game_2','trust_game','trust_game_2','survey_last'],
        #app_sequence=['survey_last'],
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []
#DEBUG = False

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = ' '
USE_POINTS = False

ROOMS = [
    dict(
        name='exp',
        display_name='exp',
        participant_label_file='_rooms/exp.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '1668040218186'

INSTALLED_APPS = ['otree']
