from datetime import datetime, timedelta
import time
from modules.driver_setup import initialize_driver
from modules.login import login, login_with_cookies
# from modules.utilities_sos import choose_hub, choose_date_sorting, choose_date_manifest, choose_date_ob
# from modules.utilities_sos import click_download_manifest, click_download_ob, click_download_sorting
from modules.helper import clear_download_folder, close_driver, get_yesterday
from processing.processing_sos import process_sorting, process_ob, process_manifest
from modules.workbook import excel_hub_performance
from constants.credential import USERNAME, PASSWORD
from constants.constant import HUB_NAMES, SORTING_FOLDER, OB_FOLDER, MANIFEST_FOLDER, DOWNLOAD_FOLDER_TMS, DOWNLOAD_FOLDER_SOS


def main():
    website = 'sos'
    days=0
    my_date = get_yesterday(days=days)

    global driver
    driver = initialize_driver(website)

    if not login_with_cookies(driver=driver, website=website):
        print("Falling back to manual login.")
        login(driver=driver, website=website, username=USERNAME, password=PASSWORD)

    clear_download_folder(DOWNLOAD_FOLDER_SOS)

    process_ob(driver=driver, hubs=HUB_NAMES, date1=my_date, date2=my_date, days=days)
    process_sorting(driver=driver, hubs=HUB_NAMES, date1=my_date, date2=my_date, days=days)
    process_manifest(driver=driver, hubs=HUB_NAMES, date1=my_date, date2=my_date, days=days)

    excel_hub_performance(day=days)

    close_driver(driver, 120)

if __name__ == "__main__":
    main()
