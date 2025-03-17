import time
import win32com.client
from constants.constant import EXCEL_HUB, EXCEL_HUB_YESTERDAY, EXCEL_SHIPMENT_V3, EXCEL_TRIP_V3

def excel_shipment(file_path):
    excel = win32com.client.Dispatch("Excel.Application")
    excel.Visible = False

    workbook = excel.Workbooks.Open(file_path)
    sheet = workbook.Sheets(1)

    # Step 1: Delete the first row
    sheet.Rows(1).Delete()
    
    # Step 2: Clear all contents in column Z
    sheet.Columns(26).ClearContents() 

    # Step 3: Write "Ghi chú" into the first row, column Z
    sheet.Cells(1, 26).Value = "Ghi chú"

    # Step 4: Save and close the workbook
    workbook.Save()
    workbook.Close(False)
    excel.Quit()
    print('Excel done!')


def excel_trip_v3():
    print('processing trip v3 excel')
    # Open Excel using COM interface
    excel = win32com.client.Dispatch("Excel.Application")
    excel.Visible = True

    # Open the workbook
    excel_file = EXCEL_TRIP_V3
    workbook = excel.Workbooks.Open(excel_file)
    print('open workbook')

    # Refresh all data connections in the workbook
    print('Refreshing...')
    workbook.RefreshAll()

    time.sleep(100)

    # Save the workbook
    workbook.Save()
    time.sleep(10)

    # Close the workbook and Excel
    workbook.Close(False)
    excel.Quit()

    print("File refreshed and saved successfully.")


def excel_shipment_v3():
    print('processing shipment partition excel')
    excel = win32com.client.Dispatch("Excel.Application")
    excel.Visible = True 

    # Open the workbook
    excel_file = EXCEL_SHIPMENT_V3
    workbook = excel.Workbooks.Open(excel_file)
    print('open workbook')

    # Refresh all data connections in the workbook
    print('Refreshing...')
    workbook.RefreshAll()

    time.sleep(60)

    # Save the workbook
    workbook.Save()
    time.sleep(10)

    print("File shipement v3 partition refreshed and saved successfully.")


def excel_hub_performance(day):
    excel = win32com.client.Dispatch("Excel.Application")
    excel.Visible = True 

    if day == 0:
        excel_file = EXCEL_HUB
    else:
        excel_file = EXCEL_HUB_YESTERDAY
        
    workbook = excel.Workbooks.Open(excel_file)

    # Refresh all data connections in the workbook
    print('Refreshing...')
    workbook.RefreshAll()

    # while excel.CalculationState != 0:  # 0 means Excel is idle (no calculation or refresh in progress)
    #     print("Refreshing...")
    #     time.sleep(10) 
    time.sleep(40)
    # Save the workbook
    workbook.Save()
    time.sleep(10)

    # # Close the workbook and Excel
    # workbook.Close(False)
    # excel.Quit()

    print("File shipement v3 partition refreshed and saved successfully.")