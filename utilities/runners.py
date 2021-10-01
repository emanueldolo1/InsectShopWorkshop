from unittest import TextTestRunner
from HtmlTestRunner import HTMLTestRunner
from utilities import config

html_test_runner = HTMLTestRunner(
    output=config.REPORTS_DIR,
    report_name=config.REPORT_NAME,
    report_title=config.PROJECT_NAME,
    combine_reports=True,
    add_timestamp=True
)

text_test_runner = TextTestRunner(verbosity=2)
