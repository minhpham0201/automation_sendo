from datetime import datetime, timedelta
import time
from modules.utilities_tms import choose_date_shipment, choose_date_trip, choose_shipment_type, click_complement_option, click_vehicle_type
from modules.utilities_tms import click_download_shipment, click_download_trip, download_export_tms
from modules.helper import  clear_download_folder, close_other_tabs, wait_crdownload
from modules.collate import collate_sorting, collate_ob, collate_manifest
from constants.constant import DOWNLOAD_FOLDER_TMS, DOWNLOAD_FOLDER_SOS



def process_shipment(driver, date1, date2):
    driver.get('https://tms.sendo.vn/OGShipment')
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 300);")
    time.sleep(1)
    choose_date_shipment(driver, date1, date2)
    choose_shipment_type(driver)
    time.sleep(5)
    click_download_shipment(driver)

    time.sleep(5)
    close_other_tabs(driver)

def process_trip(driver, date1, date2, complement=False):
    driver.get('https://tms.sendo.vn/ManageTripShuttle')
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 100);")
    choose_date_trip(driver, date1, date2)

    if complement:
        click_complement_option(driver)
        click_vehicle_type(driver)
        
    click_download_trip(driver)
        
    time.sleep(5)
    close_other_tabs(driver)


    
