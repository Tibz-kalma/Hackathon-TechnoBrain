from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    # Navigate to the login page
    driver.get("https://www.betika.com/en-ke/login")

    driver.implicitly_wait(10)

    # Find the username field
    username_field = driver.find_element(By.CSS_SELECTOR, 'input.input[type="text"]')
    username_field.send_keys("0740748285")

    # Find the password
    password_field = driver.find_element(By.CSS_SELECTOR, 'input.input[type="password"]')
    password_field.send_keys("Best3307")

    # Find login button
    login_button = driver.find_element(By.CSS_SELECTOR, 'button.button.account__payments__submit.session__form__button.login.button.button__secondary')
    login_button.click()
    
    WebDriverWait(driver, 10).until(EC.url_changes("https://www.betika.com/en-ke/login"))

    # Verify that the user is redirected to the homepage
    expected_url = "https://www.betika.com/en-ke/home" 
    WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))

    # Verify the welcome message 
    #welcome_element = WebDriverWait(driver, 10).until(
        #EC.presence_of_element_located((By.CSS_SELECTOR, "[contains(text(), 'Welcome')]"))  # Replace with actual locator
    #)

    print("Login successful and redirected to the homepage.")

finally:
    driver.quit()
