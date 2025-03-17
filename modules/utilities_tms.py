from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from constants.constant import DOWNLOAD_FOLDER_TMS
from modules.helper import wait_crdownload
from datetime import datetime


def choose_date_shipment(driver, date1, date2):
    _date1 = datetime.strptime(date1, "%B %d, %Y").strftime("%d/%m/%Y 00:00")
    _date2 = datetime.strptime(date2, "%B %d, %Y").strftime("%d/%m/%Y 23:59")

    # Combine into the final text
    date_concat = f"{_date1} - {_date2}"

    date_picker = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "ExpectedDeliveryDateStr"))
    )

    date_picker.clear()
    date_picker.send_keys(date_concat)
    date_picker.send_keys(Keys.RETURN)

def choose_shipment_type(driver):
    og_type_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "og-type"))
    )
    og_type_element.click()

   # Wait for the checkbox with value="1" to become clickable and click it
    checkbox_1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//ul[contains(@class, 'multiselect-container dropdown-menu')]//label[contains(., 'Đơn hàng không tách')]/input[@type='checkbox']")
        )
    )
    checkbox_1.click()

    checkbox_2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//ul[contains(@class, 'multiselect-container dropdown-menu')]//label[contains(., 'Đơn hàng tách(con)')]/input[@type='checkbox']")
        )
    )
    checkbox_2.click()

    body_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    body_element.click()


def click_download_shipment(driver):
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(@onclick, 'sendo.OGshipment.search()') and contains(@class, 'btn-primary')]")
        )
    )
    search_button.click()
    time.sleep(1)
    
    export_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(@onclick, 'sendo.OGshipment.showConfirmExportPopup()') and contains(., 'Xuất Vận Đơn')]")
        )
    )
    export_button.click()
    time.sleep(1)

    accept_button1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox' and @id='chk_accept' and contains(@onchange, 'sendo.OGshipment.accept')]"))
    )
    accept_button1.click()

    accept_button2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='button' and @id='btn_accept' and contains(@onclick, 'sendo.OGshipment.showExportPopup')]"))
    )
    accept_button2.click()

    export_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='button' and contains(@onclick, 'sendo.OGshipment.export')]"))
    )
    export_button.click()

    # Switch back to the original tab after confirming the download
    time.sleep(7)
    original_tab = driver.window_handles[0]
    driver.switch_to.window(original_tab)


def choose_date_trip(driver, date1, date2):
    # Wait for the date input field to become available
    date_picker = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "DateStr"))
    )
    
    date_picker.click()  # Activate the field
    date_picker.clear()
    
    # Input the new date range
    new_date_range = f"{date1} - {date2}"
    date_picker.send_keys(new_date_range)
    
    # Confirm the date selection (if needed, simulate pressing Enter or clicking outside)
    date_picker.send_keys(Keys.RETURN)
    time.sleep(2) 


def click_download_trip(driver):
    # Step 1: Click the "Xuất dữ liệu" button
    export_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@onclick='sendo.managetripshuttle.showConfirmExportPopup()' and contains(@class, 'btn btn yellow')]"))
    )

    driver.execute_script("arguments[0].click();", export_button)
    print("Clicked 'Xuất dữ liệu' button.")

    # ActionChains(driver).move_to_element(export_button).perform()
    # export_button.click()
    # print("Clicked 'Xuất dữ liệu' button.")

    # Step 2: Click the checkbox with id 'chk_accept'
    accept_checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "chk_accept"))
    )
    accept_checkbox.click()
    print("Checked the 'Tôi đã đọc và đồng ý' checkbox.")

    # Step 3: Click the "Đồng ý và tiếp tục" button
    accept_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "btn_accept"))
    )
    accept_button.click()
    print("Clicked 'Đồng ý và tiếp tục' button.")

    export_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='button' and contains(@onclick, 'sendo.managetripshuttle.export')]"))
    )
    export_button.click()

    # Switch back to the original tab after confirming the download
    time.sleep(7)
    original_tab = driver.window_handles[0]
    driver.switch_to.window(original_tab)

def click_complement_option(driver):
    dropdown = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "s2id_FilterType")))
    dropdown.click()

    complement_option = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'select2-result-label') and contains(text(), 'Chuyến có hàng bổ sung')]")))
    complement_option.click()
            
def click_vehicle_type(driver):
    dropdown = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "s2id_VehicleType")))
    dropdown.click()

    vehicle_option = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'select2-result-label') and contains(text(), 'Xe máy')]"))
        )
    vehicle_option.click()

def download_export_tms(driver):
    logs = [] 
    driver.get("https://tms.sendo.vn/Export")

    # Wait for the table to load
    table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "result-exports"))  
    )

    count = 0
    while count < 10:
        try:
            table = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "result-exports"))
            )

            rows = table.find_elements(By.XPATH, ".//tr")

            # Locate the first and second rows
            row_1 = rows[0]
            row_2 = rows[1]
            row_3 = rows[2]

            # Check the status in the third column for both rows
            status_1 = row_1.find_element(By.XPATH, ".//td[2]").text
            status_2 = row_2.find_element(By.XPATH, ".//td[2]").text
            status_3 = row_3.find_element(By.XPATH, ".//td[2]").text

            print(f"Status row 1: {status_1}, Status row 2: {status_2}, Status row 2: {status_3}")

            if status_1 == 'Hoàn thành' and status_2 == 'Hoàn thành' and status_3 == 'Hoàn thành':
                print("All 3 rows are 'Hoàn thành'. Proceeding with download.")
                break  # Exit the loop if both rows have the desired status

            else:
                print("Not all rows are 'Hoàn thành'. Refreshing page...")
                driver.refresh()
                count += 1
                print(f"Refreshed {count} times.")
                time.sleep(10)  # Wait before retrying

        except Exception as e:
            print(f"Error while checking status: {e}")
            time.sleep(5)


    try:
        # Locate and click the download link/button in row 1
        button_1 = row_1.find_element(By.XPATH, ".//td//button[contains(@onclick, 'sendo.export.download')]")
        driver.execute_script("arguments[0].click();", button_1)
        print("Downloaded file from row 1.")

        # Log the file name or URL if needed
        logs.append(button_1.get_attribute("onclick"))

        time.sleep(1)  # Slight delay before clicking the second button

        # Locate and click the download link/button in row 2
        button_2 = row_2.find_element(By.XPATH, ".//td//button[contains(@onclick, 'sendo.export.download')]")
        driver.execute_script("arguments[0].click();", button_2)
        print("Downloaded file from row 2.")

        # Log the file name or URL if needed
        logs.append(button_2.get_attribute("onclick"))

        # Locate and click the download link/button in row 3
        button_3 = row_3.find_element(By.XPATH, ".//td//button[contains(@onclick, 'sendo.export.download')]")
        driver.execute_script("arguments[0].click();", button_3)
        print("Downloaded file from row 3.")

        # Log the file name or URL if needed
        logs.append(button_3.get_attribute("onclick"))

    except Exception as e:
        print(f"Error while downloading files: {e}")


    # wait_crdownload(DOWNLOAD_FOLDER_TMS)

    return logs