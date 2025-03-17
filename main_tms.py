from datetime import datetime, timedelta
import time
import os
from modules.driver_setup import initialize_driver
from modules.login import login, login_with_cookies
from modules.utilities_tms import download_export_tms
from modules.collate import collate_shipment, collate_trip, collate_today_tms
from modules.helper import clear_download_folder, close_driver, get_yesterday, get_till_yesterday, wait_crdownload
from processing.processing_tms import process_shipment, process_trip
from modules.workbook import excel_shipment, excel_trip_v3, excel_shipment_v3
from constants.credential import USERNAME, PASSWORD
from constants.constant import DOWNLOAD_FOLDER_TMS, SHIPMENT_FOLDER_TODAY, TRIP_FOLDER, SHIPMENT_FOLDER, TRIP_COMPLEMENT_FOLDER


def main():
    website = 'tms'
    days=0
    my_date = get_yesterday(days=days)
    print(my_date)
    date1, date2 = get_till_yesterday(days=days)

    global driver
    try:
        driver = initialize_driver(website)
        
        if not login_with_cookies(driver, website=website):
            print("Falling back to manual login.")
            login(driver, website, USERNAME, PASSWORD)

        clear_download_folder(DOWNLOAD_FOLDER_TMS)

        process_trip(driver=driver, date1=date1, date2=date2, complement=True)
        process_shipment(driver=driver, date1=my_date, date2=my_date)
        process_trip(driver=driver, date1=date1, date2=date2, complement=False)
        
        download_export_tms(driver)
     
        # wait_crdownload(DOWNLOAD_FOLDER_TMS)
        time.sleep(10)
          
        collate_trip(TRIP_FOLDER, TRIP_COMPLEMENT_FOLDER)
        collate_shipment(SHIPMENT_FOLDER_TODAY, days=days)

        time.sleep(3)
        
        formatted_date = datetime.strptime(my_date, "%B %d, %Y").strftime("%d%m")
        excel_shipment(file_path=os.path.join(SHIPMENT_FOLDER_TODAY, f"{formatted_date}.csv"))
        collate_today_tms(SHIPMENT_FOLDER_TODAY, SHIPMENT_FOLDER)
        
        time.sleep(4)
        excel_trip_v3()
        excel_shipment_v3()
        
        close_driver(driver, 120)

    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
