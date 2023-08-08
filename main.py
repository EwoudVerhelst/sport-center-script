from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from enums import Sport, days, Product
from helpers import day_of_week, get_tommorow
from datetime import datetime, timedelta

#######
# Date where we want to play volleyball
TARGET_BOOK_DATE = "9/08/2023"
SPORT = Sport.BEACHVOLLEY
PRODUCT = Product.OUTDOOR
TIME = ["11:00", "12:00"]

#######


# Replace the following with your actual login credentials
USERNAME = "u0158887"
PASSWORD = "5z66MgPRD7MyBS"

# Path to the browser driver. Download the appropriate driver and provide its path.
# Example: For Chrome, download chromedriver from https://sites.google.com/a/chromium.org/chromedriver/downloads
# For Firefox, download geckodriver from https://github.com/mozilla/geckodriver/releases
DRIVER_PATH = "/home/ewoudverhelst/code-projects/sport-center-script/geckodriver"

# URL of the login page
URL = "https://usc.kuleuven.cloud/nl/members/login"


WAIT = 4


def init_driver():
    options = Options()
    options.page_load_strategy = "normal"
    # options.add_argument("headless")
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

    # Calculate the height of the viewport (visible area of the page).
    viewport_height = driver.execute_script("return window.innerHeight;")

    # Get the Y coordinate of the element on the page.
    element_y = elements[0].location["y"]

    # Calculate the vertical scroll position to center the element on the screen.
    scroll_y = element_y - (viewport_height / 2)

    # Scroll to the calculated position.
    driver.execute_script(f"window.scrollTo(0, {scroll_y});")

    time.sleep(WAIT)
    elements = driver.find_elements(
        By.XPATH,
        f"//*[@id='content']/bookable-product-index/div/bookable-product-schedule/bookable-slot-list/div/div/div/div/p/strong[contains(text(), '{time_value}')]",
    )

    print(f"found {len(elements)} elements")
    for element in elements:
        # time.sleep(WAIT)
        print(element)

        time.sleep(WAIT)
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
            reserveer_btn.click()
            time.sleep(1)
            close_btn = driver.find_element(By.CLASS_NAME, "btn-close")
            close_btn.click()
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
    date_format = "%d/%m/%Y"
    target_book_date = (datetime.strptime(TARGET_BOOK_DATE, date_format)).date()
    target_script_run_date = target_book_date - timedelta(days=1)
    today = datetime.today().date()

    print(f"target book date: {target_book_date}")
    print(f"target run date: {target_script_run_date}")
    print(f"today: {today}")

    if today != target_script_run_date:
        print("today is not the day")

    else:
        print("today is the day")

        driver = init_driver()

        login_to_webpage(driver, USERNAME, PASSWORD)

        time.sleep(WAIT)

        filter_sport_and_date(driver, SPORT.value, get_tommorow())

        time.sleep(WAIT)

        for chosen_time in TIME:
            success = find_and_reserve_element(driver, PRODUCT.value, chosen_time)
            print(f"reserve Status:  {success}")

            time.sleep(WAIT)

        driver.quit()
