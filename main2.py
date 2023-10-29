#senario1
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Set up the WebDriver with Chrome
driver = webdriver.Chrome()

# Navigate to the login page
driver.get('https://quera.org/accounts/login')

# Find the email and password input fields
email_input = driver.find_element(By.XPATH, '//*[@id="auth-container"]/div[3]/form/div[1]/div/input')
password_input = driver.find_element(By.XPATH, '//*[@id="password-input"]')

# Fill in the email and password
email_input.send_keys('kosr.dastbaz1379@gmail.com')
password_input.send_keys('kosar1379')

# Hit enter to submit the form
password_input.send_keys(Keys.ENTER)

# Wait for the page to load and check if the login was successful
time.sleep(3)

# Click on the button to navigate to https://quera.org/college/
college_button = driver.find_element(By.XPATH, '//*[@id="dashboard_widgets"]/div/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/a')
college_button.click()

# Wait for the page to load and check if the navigation was successful
driver.get('https://quera.org/college/')

# driver.execute_script("window.scrollBy(0, 3500)")
for i in range(10):
    driver.execute_script(f"window.scrollBy(0, 500)")
    time.sleep(2)

# Close the browser
driver.quit()




#please comment this code and uncomment code above to run senario1
#senario2
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# driver = webdriver.Chrome()
# driver.get('https://cse.sbu.ac.ir/')
#
# amozeshi_link = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[2]/header/div/div/div/div[2]/nav/div/div/ul/li[3]/a')
# amozeshi_link.click()
# time.sleep(5)
# form_link = driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div/ul/li[3]/div/a[3]')
# form_link.click()
#
#
# # Navigate to the login page
# driver.get('https://cse.sbu.ac.ir/form')
#
# download_link = driver.find_element(By.XPATH, '//*[@id="fragment-0-kymu"]/div/ul/li[1]/a')
# download_link.click()
#
# time.sleep(15)
# # Close the browser
# driver.quit()



#please comment this code and uncomment above to run senario1 or senario2
#senario3
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # Set up the driver
# driver = webdriver.Chrome()
# driver.get("https://www.banimode.com/")
#
# # Find the search input and enter a search query
# search_input = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.ID, "search-input"))
# )
# search_input.send_keys("عطر")
# search_input.submit()
#
# # Find the first search result and click on it
# item_link = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, "#main > div > article"))
# )
# item_link.click()
#
# # Add the item to the cart
# add_to_cart_button = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, "#product > div.app > div.product-summary-container.d-flex.bani-container > div:nth-child(1) > div > div.product-color-size-add-warranty > button"))
# )
# add_to_cart_button.click()
#
# # See the shopping cart
# shopping_cart_button = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, "#product-add-to-basket > div > div.modal-content.success > div.modal-footer > a"))
# )
# shopping_cart_button.click()
#
# # Close the browser
# time.sleep(3)
# driver.quit()
