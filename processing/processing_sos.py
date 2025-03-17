from datetime import datetime, timedelta
import time
from modules.utilities_sos import choose_hub, choose_date_sorting, choose_date_manifest, choose_date_ob
from modules.utilities_sos import click_download_manifest, click_download_ob, click_download_sorting, download_export_sos
from modules.helper import  clear_download_folder, close_other_tabs, wait_crdownload, close_driver
# from modules.utilities_tms import choose_date_shipment, choose_date_trip, choose_shipment_type
# from modules.utilities_tms import click_download_trip, click_download_shipment
from modules.collate import collate_sorting, collate_ob, collate_manifest
from constants.constant import HUB_NAMES, SORTING_FOLDER, OB_FOLDER, MANIFEST_FOLDER, DOWNLOAD_FOLDER_TMS, DOWNLOAD_FOLDER_SOS


def process_sorting(driver, hubs, date1, date2, days):
    for hub_name in hubs:
        driver.get("https://sos.sendo.vn/Commodities")
        print('go to Commodities')
        time.sleep(2)
        choose_hub(driver, hub_name)
        time.sleep(2)
        choose_date_sorting(driver, date1, date2)
        click_download_sorting(driver)
        time.sleep(1)

    time.sleep(7)
    close_other_tabs(driver)
    download_export_sos(driver)
    # wait_crdownload(DOWNLOAD_FOLDER_SOS)
    collate_sorting(SORTING_FOLDER, days=days)

def process_ob(driver, hubs, date1, date2, days):
    for hub_name in hubs:
        driver.get("https://sos.sendo.vn/outbound/index")
        print('go to Outbound')
        time.sleep(2)
        choose_hub(driver, hub_name)
        time.sleep(2)
        choose_date_ob(driver, date1, date2)
        click_download_ob(driver)
        time.sleep(1)
        
    time.sleep(7)    
    close_other_tabs(driver)
    download_export_sos(driver)
    # wait_crdownload(DOWNLOAD_FOLDER_SOS)
    collate_ob(OB_FOLDER,days=days)


def process_manifest(driver, hubs, date1, date2, days):
    for hub_name in hubs:
        driver.get("https://sos.sendo.vn/ManifestNew")
        print('go to Manifest')
        time.sleep(2)
        choose_hub(driver, hub_name)
        time.sleep(2)
        choose_date_manifest(driver, date1, date2)
        time.sleep(1)
        click_download_manifest(driver)
        time.sleep(1)
        
    time.sleep(16)
    close_other_tabs(driver)
    download_export_sos(driver)
    # wait_crdownload(DOWNLOAD_FOLDER_SOS)
    collate_manifest(MANIFEST_FOLDER, days=days)
