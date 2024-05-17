# ###############################################################
# THESE SECRET VALUES MUST BE PROVIDED:
# (this file will be ignored by Git)

FINTI_TOKEN = None
EMAIL_HOST_PASSWORD = None

assert(FINTI_TOKEN is not None, 'You MUST provide a Finti token')
# ###############################################################


# Environment choices: {DEV, TEST, PROD}
ENVIRONMENT = 'DEV'

# SECURITY WARNING: Change this and keep it a secret in production!
SECRET_KEY = '{{ secret_key }}'

# Name of machine running the application
ALLOWED_HOSTS = ['localhost']

# Debug mode (probably only true in DEV)
DEBUG = True

# SSO URL
CAS_SERVER_URL = 'https://sso-stage.oit.pdx.edu/idp/profile/cas/login'

# `````````````````
# FINTI
# `````````````````
# REQUIRED: Finti URL and Token:

FINTI_URL = 'https://sf-stage.oit.pdx.edu'

# Finti URLs (for reference)
# -  http://localhost:8888
# -  https://sf-dev.oit.pdx.edu
# -  https://sf-stage.oit.pdx.edu
# -  https://sf-prod.oit.pdx.edu

# As-of psu-base 0.11.0, Finti responses can be cached for offline development
FINTI_SIMULATE_WHEN_POSSIBLE = False   # Simulate Finti calls (i.e. when not on VPN)
FINTI_SAVE_RESPONSES = True    # Save/record actual Finti responses for offline use?

EMAIL_HOST_USER = 'cefr-app-mail'


# -----------------------------------------------------------------------------
# OPTIONAL VALUES
# -----------------------------------------------------------------------------

# You may want to disable elevated developer access while running locally
# ELEVATE_DEVELOPER_ACCESS = False

# You may want to extend session expiration during local development
# SESSION_COOKIE_AGE = 4 * 60 * 60  # 4 hours
