from utilities import cli
import definitions

# REPORTING CONSTANTS
SCREENSHOT_DIR = definitions.ROOT_DIR + "/screenshots/"
REPORTS_DIR = definitions.ROOT_DIR + "/reports/"
PROJECT_NAME = "Infinum"
REPORT_NAME = "Infinum Web Regression Test"

# ENVIRONMENTS
DEV = "dev"
STAGING = "staging"

# ENVIRONMENT CONSTANTS
URLS = {DEV: "https://beta.infinum.com", STAGING: "https://infinum.co"}

# DRIVER CONSTANTS
DRIVER_TIMEOUT = 30

# DERIVED CONSTANTS
ARGS = cli.get_cli_args()

BROWSER = ARGS.browser
ENV = ARGS.env
REPORT = ARGS.report
SCOPE = ARGS.scope

BASE_URL = URLS[ENV]
