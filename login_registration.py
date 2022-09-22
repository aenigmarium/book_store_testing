import time
from selenium import webdriver # импортируем webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')

#Scenario 2: Account registration
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
my_account = driver.find_element_by_css_selector('.menu-item-type-post_type:nth-child(2)')
my_account.click()
email_value = driver.find_element_by_id('reg_email')
email_value.click()
email_value.send_keys('testmail7@blahblah.com')
pass_value = driver.find_element_by_id('reg_password')
pass_value.click()
pass_value.send_keys('!p@s$w0Rd!m')
pass_value.click()
register_btn = driver.find_element_by_css_selector('div.u-column2 [type="password"]')
password_str = WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-password-strength"), 'Medium'))
register_btn.click()
time.sleep(5)

#Scenario 3: System Login
driver.get("http://practice.automationtesting.in/")
my_account = driver.find_element_by_css_selector('.menu-item-type-post_type:nth-child(2)')
my_account.click()
email_login = driver.find_element_by_id('username')
email_login.send_keys('testmail@blahblah.com')
pass_login = driver.find_element_by_id('password')
pass_login.send_keys('!p@s$w0Rd!M')
login_btn = driver.find_element_by_css_selector('[name="login"]')
login_btn.click()
logout_btn = driver.find_element_by_class_name('woocommerce-MyAccount-navigation-link--customer-logout')
logout_btn_txt = logout_btn.text
assert 'Logout' in logout_btn_txt
