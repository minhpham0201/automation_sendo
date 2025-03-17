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
from constants.constant import DOWNLOAD_FOLDER_TMS, SHIPMENT_FOLDER_TODAY, TRIP_FOLDER, SHIPMENT_FOLDER


if __name__ == "__main__":
    collate_shipment(SHIPMENT_FOLDER)
    