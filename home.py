import time
from selenium import webdriver # импортируем webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')

#Scenario 1: Commentary add
driver.get("http://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);")
book_title = driver.find_element_by_tag_name('h3')
book_title.click()
reviews = driver.find_element_by_class_name('reviews_tab')
reviews.click()
fivestars = driver.find_element_by_class_name('star-5')
fivestars.click()
comment_box = driver.find_element_by_id('comment')
comment_box.send_keys('Amazing book!')
name = driver.find_element_by_id('author')
name.send_keys('Test')
email_value = driver.find_element_by_id('email')
email_value.send_keys('test@testmail.com')
submit_btn = driver.find_element_by_class_name('submit')
submit_btn.click()
#driver.quit()