import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
from datetime import datetime

import pytest
import undetected_chromedriver as uc


@pytest.fixture
def setup():
    options = uc.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = uc.Chrome(options=options, headless=False, detach=True)
    driver.implicitly_wait(10)
    return driver

# @pytest.fixture()
# def setup():
#     chrome_options = Options()
#     chrome_options.add_experimental_option("detach", True)
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
#         options=chrome_options)
#     return driver



########### pytest HTML Report ################

def pytest_configure(config):
    # Ensure the Reports folder exists
    os.makedirs("Reports", exist_ok=True)

    # Define dynamic HTML report file path
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_file = f"Reports/test_report_{timestamp}.html"

    # Assign the path to the config.option.html if it exists
    if hasattr(config.option, "htmlpath") and config.option.htmlpath is None:
        config.option.htmlpath = report_file

    config._metadata = {
            "Project Name": "NopCommerce UI Automation",
            "Tester": "Temitope Ayannusi",
            "Application": "nopCommerce Demo",
            "Browser": "Chrome (undetected)" }

    def pytest_html_report_title(report):
        report.title = "Automation Test Report - NopCommerce"





# Hook to add screenshot on test failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("Reports/failures") else "w"
        try:
            if "driver" in item.funcargs:
                web_driver = item.funcargs["driver"]
                screenshot_dir = "Screenshots"
                os.makedirs(screenshot_dir, exist_ok=True)
                file_name = os.path.join(screenshot_dir, f"{item.name}.png")
                web_driver.save_screenshot(file_name)

                # Attach screenshot to report
                extra = getattr(rep, "extra", [])
                extra.append(pytest_html.extras.image(file_name))
                rep.extra = extra
        except Exception as e:
            print(f"Error saving screenshot: {e}")












# It is hook for Adding Environment info to HTML Report
# def pytest_addoption(parser):
#     # Define custom report output path
#     timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#     report_file = f"Reports/test_report_{timestamp}.html"
#     parser.addoption("--html", action="store", default=report_file, help="HTML report path")
#
# def pytest_configure(config):
#     # Ensure the Reports folder exists
#     os.makedirs("Reports", exist_ok=True)







