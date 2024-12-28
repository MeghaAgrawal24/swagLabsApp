import pytest
from selenium import webdriver

@pytest.fixture
def setup(browser):
    if browser == "chrome":
        driver= webdriver.Chrome()
        print("******Launching Chrome Browser******")
    elif browser == "firefox":
        driver= webdriver.Firefox()
        print("******Launching Firefox Browser******")
    else:
        driver= webdriver.Chrome()
    
    return driver

def pytest_addoption(parser): #This will get the values from CLI hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): # This will return the browser value to setup method
    return request.config.getoption("--browser")

################Pytest Html Report ######################

# Hook for customizing the HTML report title
def pytest_html_report_title(report):
    report.title = "Swag Labs Test Report"  # Set a custom title for the HTML report

#It is a hook for deleting/modifying environment info to the html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)