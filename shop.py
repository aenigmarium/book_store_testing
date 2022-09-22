import time
from selenium import webdriver # импортируем webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()

#Scenario 4: Displaying product page
driver.get("http://practice.automationtesting.in/")
my_account = driver.find_element_by_css_selector('.menu-item-type-post_type:nth-child(2)')
my_account.click()
email_login = driver.find_element_by_id('username')
email_login.send_keys('testmail@blahblah.com')
pass_login = driver.find_element_by_id('password')
pass_login.send_keys('!p@s$w0Rd!M')
login_btn = driver.find_element_by_css_selector('[name="login"]')
login_btn.click()
shop = driver.find_element_by_id('menu-item-40')
shop.click()
html5book = driver.find_element_by_partial_link_text('HTML5 Forms')
html5book.click()
html5title = driver.find_element_by_class_name('entry-title').text
assert 'HTML5 Forms' in html5title

#Scenario 5: amount of products in the category
driver.get("http://practice.automationtesting.in/")
# my_account = driver.find_element_by_css_selector('.menu-item-type-post_type:nth-child(2)')
# my_account.click()
# email_login = driver.find_element_by_id('username')
# email_login.send_keys('testmail@blahblah.com')
# pass_login = driver.find_element_by_id('password')
# pass_login.send_keys('!p@s$w0Rd!M')
# login_btn = driver.find_element_by_css_selector('[name="login"]')
# login_btn.click()
shop = driver.find_element_by_id('menu-item-40')
shop.click()
time.sleep(1)
html_filter = driver.find_element_by_link_text('HTML')
html_filter.click()
included_product = driver.find_elements_by_class_name('woocommerce-LoopProduct-link')
assert len(included_product) == 3

#Scenario 6: Product sorting
driver.get("http://practice.automationtesting.in/")
# my_account = driver.find_element_by_css_selector('.menu-item-type-post_type:nth-child(2)')
# my_account.click()
# email_login = driver.find_element_by_id('username')
# email_login.send_keys('testmail@blahblah.com')
# pass_login = driver.find_element_by_id('password')
# pass_login.send_keys('!p@s$w0Rd!M')
# login_btn = driver.find_element_by_css_selector('[name="login"]')
# login_btn.click()
shop = driver.find_element_by_id('menu-item-40')
shop.click()
default_selector = driver.find_element_by_css_selector('[value="menu_order"]')
default_value = default_selector.get_attribute('selected')
if default_value is not None:
    print('Default value is selected')
else:
    print('Default value is not selected')
selector_sorting = driver.find_element_by_class_name('orderby')
select_sorting = Select(selector_sorting)
select_sorting.select_by_visible_text("Sort by price: high to low")
new_value = driver.find_element_by_css_selector('[value="price-desc"]')
selected_value = new_value.get_attribute('selected')
if selected_value is not None:
    print('Value has been selected')
else:
    print('Default value has not been selected')

#Scenario 7: Product display, price discount
driver.get("http://practice.automationtesting.in/")
# my_account = driver.find_element_by_css_selector('.menu-item-type-post_type:nth-child(2)')
# my_account.click()
# email_login = driver.find_element_by_id('username')
# email_login.send_keys('testmail@blahblah.com')
# pass_login = driver.find_element_by_id('password')
# pass_login.send_keys('!p@s$w0Rd!M')
# login_btn = driver.find_element_by_css_selector('[name="login"]')
# login_btn.click()
shop = driver.find_element_by_id('menu-item-40')
shop.click()
android_book = driver.find_element_by_partial_link_text('Android Quick Start Guide')
android_book.click()
former_price = driver.find_element_by_css_selector('.price > del > .woocommerce-Price-amount')
current_price = driver.find_element_by_css_selector('.price > ins > .woocommerce-Price-amount')
assert former_price.text == '₹600.00'
assert current_price.text == '₹450.00'
cover = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@class="images"]')))
cover.click()
close_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'pp_close')))
close_btn.click()
# driver.close()

#Scenario 8: Checking price in the cart
driver.get("http://practice.automationtesting.in/")
shop = driver.find_element_by_id('menu-item-40')
shop.click()
basket_add = driver.find_element_by_css_selector('[data-product_id="182"]')
basket_add.click()
time.sleep(3)
cart_count = driver.find_element_by_css_selector('.wpmenucart-contents > .cartcontents')
amount = driver.find_element_by_class_name('amount')
assert cart_count.text == "1 Item"
assert amount.text == "₹180.00"
cart_count.click()
subtotal = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.CLASS_NAME, 'cart-subtotal')))
total = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.CLASS_NAME, 'order-total')))
assert subtotal.text == 'Subtotal ₹180.00'
assert total.text == 'Total ₹183.60'
# driver.close()

#Scenario 9: Shop: working with the cart
driver.get("http://practice.automationtesting.in/")
shop = driver.find_element_by_id('menu-item-40')
shop.click()
basket_add = driver.find_element_by_css_selector('[data-product_id="182"]')
basket_add.click()
time.sleep(3)
basket_add_jsbook = driver.find_element_by_css_selector('[data-product_id="180"]')
basket_add_jsbook.click()
time.sleep(3)
cart = driver.find_element_by_class_name('wpmenucart-contents')
cart.click()
time.sleep(3)
remove_1stbook = driver.find_element_by_css_selector('.cart_item:nth-child(1) > .product-remove > .remove')
remove_1stbook.click()
time.sleep(3) #maybe explicit wait should be added
undo_btn = driver.find_element_by_partial_link_text('Undo?')
undo_btn.click()
book1_quantity = driver.find_element_by_css_selector('.cart_item:nth-child(1) > .product-quantity > .quantity > .qty')
book1_quantity.clear()
book1_quantity.send_keys(3)
update_basket = driver.find_element_by_css_selector('[name="update_cart"]')
update_basket.click()
time.sleep(3) #maybe explicit wait should be added
book1_quantity_value = driver.find_element_by_css_selector('.cart_item:nth-child(1) > .product-quantity > .quantity > [type="number"]')
book1_quantity_attribute = book1_quantity_value.get_attribute('value')
assert book1_quantity_attribute == ('3')
time.sleep(3)
coupon_btn = driver.find_element_by_css_selector('.coupon > .button')
coupon_btn.click()
time.sleep(3) #probably explicit wait shoud be added
coupon_msg = driver.find_element_by_css_selector('.woocommerce-error')
print(coupon_msg.text)
# driver.close()

#Scenario 10: Shop: buying a product
driver.get("http://practice.automationtesting.in/")
shop = driver.find_element_by_id('menu-item-40')
shop.click()
driver.execute_script("window.scrollBy(0, 300);")
basket_add = driver.find_element_by_css_selector('[data-product_id="182"]')
basket_add.click()
time.sleep(3)
cart = driver.find_element_by_css_selector('.wpmenucart-display-standard')
cart.click()
checkout = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.checkout-button')))
checkout.click()
first_name = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.ID, 'billing_first_name')))
first_name.send_keys('Test')
second_name = driver.find_element_by_id('billing_last_name')
second_name.send_keys('Testovich')
email_value = driver.find_element_by_id('billing_email')
email_value.send_keys('test@testmail.com')
phone_value = driver.find_element_by_id('billing_phone')
phone_value.send_keys('77777777')
country = driver.find_element_by_id('s2id_billing_country')
country.click()
search_box = driver.find_element_by_id('s2id_autogen1_search')
search_box.send_keys('Isle')
result = driver.find_element_by_class_name('select2-result-label')
result.click()
address = driver.find_element_by_css_selector('#billing_address_1:nth-child(2)')
address.send_keys('Test')
city = driver.find_element_by_id('billing_city')
city.send_keys('Test')
postcode = driver.find_element_by_id('billing_postcode')
postcode.send_keys('11111111')
state_value = driver.find_element_by_css_selector('#billing_state:nth-child(2)')
state_value.send_keys('Isle of Man')
driver.execute_script("window.scrollBy(0, 400);")
time.sleep(2)
radio = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.payment_method_cheque > .input-radio')))
radio.click()
place_order = driver.find_element_by_css_selector(".alt:nth-child(2)")
place_order.click()
received_order = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, 'woocommerce-thankyou-order-received')))
print(received_order.text)
payment_method = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, 'method')))
print(payment_method.text)
driver.close()




