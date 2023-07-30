from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from enums import Sport, days, Product
from helpers import day_of_week, get_tommorow

# Replace the following with your actual login credentials
USERNAME = "u0158887"
PASSWORD = "5z66MgPRD7MyBS"

# Path to the browser driver. Download the appropriate driver and provide its path.
# Example: For Chrome, download chromedriver from https://sites.google.com/a/chromium.org/chromedriver/downloads
# For Firefox, download geckodriver from https://github.com/mozilla/geckodriver/releases
DRIVER_PATH = "/home/ewoudverhelst/code-projects/sport-center-script/geckodriver"

# URL of the login page
URL = "https://usc.kuleuven.cloud/nl/members/login"

# Sport and date
SPORT = Sport.BEACHVOLLEY
PRODUCT = Product.INDOOR
TOMOROW = get_tommorow()
TIME = "08:00"

WAIT = 8


def init_driver():
    options = Options()
    options.page_load_strategy = "normal"
    driver = webdriver.Chrome(options=options)
    driver.get(URL)
    return driver


def filter_sport_and_date(driver, sport, date):
    # Select sport type and date
    sport_selection = driver.find_element(by=By.LINK_TEXT, value=sport)
    sport_selection.click()

    date_selector = driver.find_element(By.XPATH, f"//span[contains(text(), '{date}')]")
    date_selector.click()

    time.sleep(WAIT)


def find_and_reserve_element(driver, product, time_value):
    # Find all the elements that match the sport and time criteria

    elements = driver.find_elements(
        By.XPATH,
        f"//*[@id='content']/bookable-product-index/div/bookable-product-schedule/bookable-slot-list/div/div/div/div/p/strong[contains(text(), '{time_value}')]",
    )

    while len(elements) == 0:
        elements = driver.find_elements(
            By.XPATH, f"//strong[contains(text(), '{time_value}')]"
        )

    print(f"found {len(elements)} elements")
    for element in elements:
        print(element)
        element.click()
        print("element clicked")

        time.sleep(WAIT)

        modal_title = driver.find_element(By.CLASS_NAME, "modal-title")
        product_str = modal_title.text

        if not product_str.lower() == product.lower():
            print("wrong product")
            close_btn = driver.find_element(By.CLASS_NAME, "btn-close")
            close_btn.click()
            time.sleep(1)
        else:
            print(f"found right product: {product_str}")
            reserveer_btns = driver.find_elements(By.CLASS_NAME, "btn-primary")
            print(f"found {len(reserveer_btns)} reserveer buttons")
            reserveer_btn = reserveer_btns[-1]
            # reserveer_btn.click()
            return True

    time.sleep(WAIT)
    return False


def login_to_webpage(driver, username, password):
    driver.implicitly_wait(WAIT)

    authenticator_btn = driver.find_element(
        By.XPATH, f"//span[contains(text(), 'KU Leuven Authenticator')]"
    )
    authenticator_btn.click()

    time.sleep(WAIT)

    # Find the email and password input fields and enter the credentials

    email_field = driver.find_element(by=By.ID, value="username")
    email_field.send_keys(username)

    password_field = driver.find_element(by=By.ID, value="password")
    password_field.send_keys(password)

    # # Submit the form
    submit_button = driver.find_element(by=By.ID, value="pwdLoginBtn")
    submit_button.click()

    # Wait for some time to let the page load (you can use better waiting techniques)
    while (
        driver.current_url
        != "https://usc.kuleuven.cloud/products/bookable-product-schedule"
    ):
        time.sleep(WAIT)


if __name__ == "__main__":
    driver = init_driver()

    login_to_webpage(driver, USERNAME, PASSWORD)

    time.sleep(WAIT)

    filter_sport_and_date(driver, SPORT.value, TOMOROW)

    time.sleep(WAIT)

    success = find_and_reserve_element(driver, PRODUCT.value, TIME)

    print(f"reserve Status:  {success}")

    time.sleep(WAIT)

    driver.quit()
