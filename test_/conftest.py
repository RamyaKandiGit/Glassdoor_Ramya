import pytest
from selenium import webdriver
from Library.config import Config
from selenium.webdriver.firefox.options import Options

@pytest.fixture(params=["Chrome","Edge"])

def _driver(request):
    if request.param == "Chrome":
        driver = webdriver.Chrome(Config.Chrome_Driver_Path)

    # elif request.param == "Firefox":
    #     options = Options()
    #     options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    #     driver = webdriver.Firefox(executable_path=Config.Gecko_Driver_Path,options=options)

    elif request.param == "Edge":
        driver = webdriver.Edge(Config.Edge_Driver_Path)


    driver.get(Config.URL)
    driver.maximize_window()
    driver.implicitly_wait(60)
    yield driver
    print(driver.title)
    driver.save_screenshot("test_module.png")
    driver.close()