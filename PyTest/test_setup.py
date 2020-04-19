from selenium import webdriver

def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path="/Users/gailphillips/PycharmProjects/automationpractice/venv/bin/chromedriver")
    driver.get("http://www.automationpractice.com")

def test_login():
    driver.find_element_by_class_name("login").click()
    driver.maximize_window()
    driver.find_element_by_id('email').send_keys("test.testtown@gmail.com")
    driver.find_element_by_id("passwd").send_keys("12345678")
    driver.find_element_by_id('SubmitLogin').click()

#if_name_==_main_
def test_teardown():
    driver.close()

def test_successmessage():
    print("all tests passed")