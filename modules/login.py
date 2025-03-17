from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle


def login(driver, website, username, password):
    if website == 'sos':
        driver.get("https://sos.sendo.vn")
    elif website == 'tms':
        driver.get("https://tms.sendo.vn")

    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Đăng Nhập - Login')]"))
    )
    login_button.click()

    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))
    )
    email_field.send_keys(username)
    email_field.send_keys(Keys.RETURN)

    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@type='password']"))
    )
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)

    if website == 'sos':
        WebDriverWait(driver, 120).until(
        EC.url_contains("https://sos.sendo.vn")
    )
        
        with open("cookies_sos.pkl", "wb") as file:
            pickle.dump(driver.get_cookies(), file)
        print("Logged in and cookies saved.")

    elif website == 'tms':
        WebDriverWait(driver, 120).until(
        EC.url_contains("https://tms.sendo.vn")
    )
        with open("cookies_tms.pkl", "wb") as file:
            pickle.dump(driver.get_cookies(), file)
        print("Logged in and cookies saved.")


def login_with_cookies(driver, website):
    if website == 'sos':
        try:
            driver.get("https://sos.sendo.vn")

            with open("cookies_sos.pkl", "rb") as file:
                cookies = pickle.load(file)
                for cookie in cookies:
                    driver.add_cookie(cookie)

            driver.refresh()

            # Confirm login by checking for a specific element unique to logged-in users
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='navbar-container d-flex content']"))
            )
            print("Logged in using cookies.")
            return True
        
        except Exception as e:
            print(f"Failed to log in using cookies: {e}")
            return False
        
    elif website == 'tms':
        try:
            driver.get("https://tms.sendo.vn")

            # Load cookies
            with open("cookies_tms.pkl", "rb") as file:
                cookies = pickle.load(file)
                for cookie in cookies:
                    driver.add_cookie(cookie)

            driver.refresh()

            WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "page-logo"))
        )
            print("'page-logo' element is present.")
            return True
    
        except Exception as e:
            print(f"Failed to log in using cookies: {e}")
            return False
