import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help='''Select a language.\n
                     The options are: \n
                     -- Russian: ru, \n
                     -- English: en, \n
                     -- French: fr, \n
                     -- Spanish: sp.''')


@pytest.fixture(scope='function')
def browser(request):
    browser_lang = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages':
                                              browser_lang})
    browser = webdriver.Chrome(options=options)
    yield browser
    time.sleep(3)
    print('\n Quitting the browser in progress...')
    browser.quit()