from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime, timedelta
from constants.constant import LAST_DATE_OF_MONTH
from modules.helper import wait_crdownload
from constants.constant import DOWNLOAD_FOLDER_SOS


def choose_hub(driver, hub_name):
    select_hub = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "select2-selection__rendered"))
    )

    # Click the dropdown to open the options
    select_hub.click()
    time.sleep(1)

    # Wait until the specific hub option is displayed and click it
    hub_option = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, f"//li[text()='{hub_name}']"))
    )
    hub_option.click()
    print(f"Selected the hub: {hub_name}.")
    time.sleep(1)


def choose_date_sorting(driver, date1, date2):
    date_picker = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "fp-range"))
    )
    date_picker.click()
    time.sleep(1)

    day_month1 = date1.split(',')[0]

    # Check if date1 is the last date of the month
    if day_month1 in LAST_DATE_OF_MONTH:
        print('choose prev calendar month')
        prev_month_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'flatpickr-prev-month'))
        )
        prev_month_button.click()
        time.sleep(1)

    print('choose date 1')    
    specific_date = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//span[contains(@class, 'flatpickr-day') and @aria-label='{date1}']"))
    )
    specific_date.click()


    specific_date = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//span[contains(@class, 'flatpickr-day') and @aria-label='{date2}']"))
    )
    specific_date.click()

def choose_date_ob(driver, date1, date2):
    try:
        # Wait for the date picker to be present and click it
        date_picker = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "fp-range-2"))
        )
        date_picker.click()

        day_month1 = date1.split(',')[0]
        # Check if date1 is the last date of the month
        if day_month1 in LAST_DATE_OF_MONTH:
            prev_month_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((
                        By.XPATH, 
            "//div[contains(@class, 'flatpickr-calendar') and contains(@class, 'rangeMode') and contains(@style, 'left: auto')]"
            "//span[contains(@class, 'flatpickr-prev-month')]")))
            prev_month_button.click()
            time.sleep(1)

        # Select the first date inside the div with 'style' containing 'left: auto'
        specific_date1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, 
                f"//div[contains(@style, 'left: auto')]//span[contains(@class, 'flatpickr-day') and @aria-label='{date1}']"
            ))
        )
        specific_date1.click()
        

        # Select the second date inside the div with 'style' containing 'left: auto'
        specific_date2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, 
                f"//div[contains(@style, 'left: auto')]//span[contains(@class, 'flatpickr-day') and @aria-label='{date2}']"
            ))
        )
        specific_date2.click()
    
    except Exception as e:
        print(f"Error selecting dates: {e}")
        return

def choose_date_manifest(driver, date1, date2):
    date_picker = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "fp-range-2"))
    )
    date_picker.click()
    time.sleep(2)

    day_month1 = date1.split(',')[0]

    # Check if date1 is the last date of the month
    if day_month1 in LAST_DATE_OF_MONTH:
        print('choose prev calendar month')
        prev_month_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'flatpickr-prev-month'))
        )
        prev_month_button.click()
        time.sleep(1)

    print('choose date 1')    
    specific_date = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//span[contains(@class, 'flatpickr-day') and @aria-label='{date1}']"))
    )
    specific_date.click()
    time.sleep(1)


    specific_date = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//span[contains(@class, 'flatpickr-day') and @aria-label='{date2}']"))
    )
    specific_date.click()

def click_download_sorting(driver):
    # Look for the search button by ID and click it
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "search-button"))
    )
    search_button.click()
    time.sleep(1)

    danger_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn btn-outline-danger waves-effect')]"))
    )
    danger_button.click()
    time.sleep(1)

    # Wait for the small popup to appear and select the checkbox by ID
    popup_label = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "checkdetail2"))
    )
    popup_label.click()
    time.sleep(1)

    # Look for the primary confirmation button and click it
    confirm_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn btn-primary waves-effect waves-float waves-light')]"))
    )
    confirm_button.click()
    print("File downloading")
    time.sleep(5)

    # Switch back to the original tab after confirming the download
    original_tab = driver.window_handles[0]
    driver.switch_to.window(original_tab)


def click_download_ob(driver):
    danger_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn btn-outline-danger ms-1 waves-effect')]"))
    )
    danger_button.click()
    time.sleep(1)

    confirm_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn btn-primary waves-effect waves-float waves-light')]"))
    )
    confirm_button.click()
    print("File downloading")
    time.sleep(5)

    # Switch back to the original tab after confirming the download
    original_tab = driver.window_handles[0]
    driver.switch_to.window(original_tab)


def click_download_manifest(driver):
    danger_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn btn-outline-danger waves-effect')]"))
    )
    danger_button.click()
    time.sleep(1)

    confirm_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'btn btn-primary waves-effect waves-float waves-light')]"))
    )

    # Use JavaScript to execute the button's onclick function directly
    driver.execute_script("view.exportData()")
    print("File downloading")
    time.sleep(5)
    # # Switch back to the original tab after confirming the download
    original_tab = driver.window_handles[0]
    driver.switch_to.window(original_tab)


def download_export_sos(driver):
    logs = []

    driver.get("https://sos.sendo.vn/exportlogs/index")

    # Wait for the table with ID 'export-datatable' to load
    table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "export-datatable"))
    )

    rows = table.find_elements(By.XPATH, ".//tr")
    # Get today's date in the required format
    today = datetime.now().strftime("%d/%m/%Y")

    count = 0
    while count < 5:
        try:
            table = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "export-datatable"))
            )

            row_1 = table.find_elements(By.XPATH, ".//tr")[0]
         
            status = row_1.find_element(By.XPATH, ".//td[3]//span").text

            if "Thành công" in status:
                print("The first row status 'Thành công'.")
                break  

            else:
                print("The first row status 'Đang xử lý'. Refreshing page...")
                driver.refresh()
                count += 1
                print(f'refresh {count} time')
                time.sleep(10)
               

        except Exception as e:
            print(f"Error while checking status: {e}")
            time.sleep(5)

    # Once all rows have the status "Thành công", proceed to download files
    rows = table.find_elements(By.XPATH, ".//tr")

    for i, row in enumerate(reversed(rows[:6])):  # Limit to top 6 rows
        try:
            # Check if the row contains today's date
            if today not in row.text:
                continue

            # Find the download link
            link = row.find_element(By.XPATH, ".//a[contains(@href, 'http')]")
            download_url = link.get_attribute("href")

            file_name = download_url.split('/')[-1]
            logs.append(file_name)

            # Click the link to start the download (it will open a new tab)
            driver.execute_script("arguments[0].click();", link)
            print(f"Started downloading file from row {6-i}: {download_url}")

            time.sleep(1)

        except Exception as e:
            print(f"Could not process row {6-i}: {e}")
    
    wait_crdownload(DOWNLOAD_FOLDER_SOS)

    return logs





