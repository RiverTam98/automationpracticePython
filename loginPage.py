from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.automationpractice.com")

driver.find_element_by_class_name("login").click()
driver.maximize_window()
driver.find_element_by_id('email').send_keys("test.testtown@gmail.com")
driver.find_element_by_id("passwd").send_keys("12345678")
driver.find_element_by_id('SubmitLogin').click()

#if_name_==_main_

#driver.close()

print("all tests passed")