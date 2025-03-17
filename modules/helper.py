import glob
import os 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime, timedelta


def get_yesterday(days=1):
    yesterday = datetime.now() - timedelta(days=days)
    day = yesterday.day
    my_date = yesterday.strftime(f"%B {day}, %Y")

    return my_date

def get_till_yesterday(days=1):
    now = datetime.now()
    date1 = now.replace(day=1, hour=0, minute=0, second=0).strftime("%d/%m/%Y %H:%M")

    yesterday = now - timedelta(days=days)
    date2 = yesterday.replace(hour=23, minute=59, second=0).strftime("%d/%m/%Y %H:%M")
    
    return date1, date2

def wait_crdownload(download_dir):
    while True:
        incomplete_files = [f for f in os.listdir(download_dir)
            if os.path.exists(os.path.join(download_dir, f)) and f.endswith(".crdownload")]
        
        print('incomplete', incomplete_files)

        if not incomplete_files:
            print('No CRDownload files')
            break

        time.sleep(2)
    
            
def clear_download_folder(folder_path):
    files = glob.glob(os.path.join(folder_path, "*"))
    for file in files:
        os.remove(file)


def close_other_tabs(driver):
    # Get all window handles (tabs)
    window_handles = driver.window_handles
    
    # Ensure there is more than one tab
    if len(window_handles) > 1:
        # Loop through all tabs except the first one
        for handle in window_handles[1:]:
            # Switch to the tab and close it
            driver.switch_to.window(handle)
            driver.close()
        
        # Switch back to the first tab
        driver.switch_to.window(window_handles[0])

def close_driver(driver, sleep):
    print(f'closing driver in {sleep} minutes')
    time.sleep(sleep)
    driver.quit()