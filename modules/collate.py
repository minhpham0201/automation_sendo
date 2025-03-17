import os
import shutil
import glob
from datetime import datetime, timedelta
import zipfile
from constants.constant import DOWNLOAD_FOLDER_SOS, DOWNLOAD_FOLDER_TMS

def collate_sorting(destination_dir, days):
    # Directories
    current_dir = DOWNLOAD_FOLDER_SOS

    # Get yesterday's date in the format 'ddmm'
    yesterday = datetime.now() - timedelta(days=days)
    yesterday_str = yesterday.strftime('%d%m')

    # Get today's date
    today = datetime.now().date()

    print(f"Yesterday's date: {yesterday_str}")

    # Expected filenames for sorting
    sorting_filenames = [
        f"{yesterday_str}_hsnb",
        f"{yesterday_str}_hbta",
        f"{yesterday_str}_hs12",
        f"{yesterday_str}_hba",
        f"{yesterday_str}_hbc",
        f"{yesterday_str}_hbb"
    ]

    # Get all .csv files in the 'Downloaded' directory
    csv_files = glob.glob(os.path.join(current_dir, '*.csv'))

    # Filter files created today
    csv_files_today = [
        file for file in csv_files if datetime.fromtimestamp(os.path.getctime(file)).date() == today
    ]

    print(f"CSV files created today: {len(csv_files_today)}")

    # Sort the files by creation date
    csv_files_today.sort(key=os.path.getctime)

    # Ensure that the number of sorting filenames matches the number of today's CSV files
    if len(csv_files_today) == len(sorting_filenames):
        for i in range(len(csv_files_today)):
            # Get the current file path
            current_file_path = csv_files_today[i]
            
            # Define the new file path with the new name
            new_file_name = os.path.join(destination_dir, sorting_filenames[i] + '.csv')
            
            # Rename the file
            os.rename(current_file_path, new_file_name)
            print(f'Renamed: {current_file_path} to {new_file_name}')
    else:
        print("The number of sorting filenames does not match the number of CSV files.")


def collate_ob(destination_dir, days):
    current_dir = DOWNLOAD_FOLDER_SOS

    yesterday = datetime.now() - timedelta(days=days)
    yesterday_str = yesterday.strftime('%d%m')

    today = datetime.now().date()

    print(f"Yesterday's date in 'ddmm' format: {yesterday_str}")

    # Expected filenames for renaming
    ob_filenames = [
        f"{yesterday_str}_hsnb.csv",
        f"{yesterday_str}_hbta.csv",
        f"{yesterday_str}_hs12.csv",
        f"{yesterday_str}_hba.csv",
        f"{yesterday_str}_hbc.csv",
        f"{yesterday_str}_hbb.csv"
    ]

    # Get all .zip files in the 'Downloaded' directory
    zip_files = glob.glob(os.path.join(current_dir, '*.zip'))

    # Filter .zip files created today
    zip_files_today = [
        file for file in zip_files if datetime.fromtimestamp(os.path.getctime(file)).date() == today
    ]

    # Sort the .zip files by creation time
    zip_files_today.sort(key=os.path.getctime)

    # Check if the number of .zip files matches the number of expected filenames
    if len(zip_files_today) == len(ob_filenames):
        for i, zip_file in enumerate(zip_files_today):
            with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                # Extract the single file from the .zip directly to destination_dir
                extracted_file = zip_ref.namelist()[0]
                zip_ref.extract(extracted_file, destination_dir)
                print(f"Extracted: {zip_file} to {destination_dir}")

            # Construct full paths for the extracted and renamed files
            extracted_file_path = os.path.join(destination_dir, extracted_file)
            renamed_file_path = os.path.join(destination_dir, ob_filenames[i])

            # Check if the renamed file already exists
            if os.path.exists(renamed_file_path):
                print(f"File already exists: {renamed_file_path}. Skipping.")
                # Remove the .zip file since it was processed
                os.remove(zip_file)
                print(f"Removed .zip file: {zip_file}")
                continue

            # Rename the extracted file
            os.rename(extracted_file_path, renamed_file_path)
            print(f"Renamed: {extracted_file_path} to {renamed_file_path}")

            # Remove the .zip file after extraction and renaming
            os.remove(zip_file)
            print(f"Removed .zip file: {zip_file}")
    else:
        print("The number of .zip files does not match the number of expected filenames.")


def collate_manifest(destination_dir, days):
    # Directories
    current_dir = DOWNLOAD_FOLDER_SOS

    # Get yesterday's date in the format 'ddmm'
    yesterday = datetime.now() - timedelta(days=days)
    yesterday_str = yesterday.strftime('%d%m')

    # Get today's date
    today = datetime.now().date()

    print(f"Yesterday's date: {yesterday_str}")

    # Expected filenames for sorting
    manifest_filenames = [
        f"{yesterday_str}_hsnb",
        f"{yesterday_str}_hbta",
        f"{yesterday_str}_hs12",
        f"{yesterday_str}_hba",
        f"{yesterday_str}_hbc",
        f"{yesterday_str}_hbb"
    ]

    # Get all .csv files in the 'Downloaded' directory
    csv_files = glob.glob(os.path.join(current_dir, '*.csv'))

    # Filter files created today
    csv_files_today = [
        file for file in csv_files if datetime.fromtimestamp(os.path.getctime(file)).date() == today
    ]

    print(f"CSV files created today: {len(csv_files_today)}")

    # Sort the files by creation date
    csv_files_today.sort(key=os.path.getctime)

    # Ensure that the number of sorting filenames matches the number of today's CSV files
    if len(csv_files_today) == len(manifest_filenames):
        for i in range(len(csv_files_today)):
            # Get the current file path
            current_file_path = csv_files_today[i]
            
            # Define the new file path with the new name
            new_file_name = os.path.join(destination_dir, manifest_filenames[i] + '.csv')
            
            # Rename the file
            os.rename(current_file_path, new_file_name)
            print(f'Renamed: {current_file_path} to {new_file_name}')
    else:
        print("The number of manifest filenames does not match the number of CSV files.")


def collate_shipment(destination_dir, days):
    print('collate shipment')
    current_dir = DOWNLOAD_FOLDER_TMS
    print(current_dir)

    yesterday = datetime.now() - timedelta(days=days)
    yesterday_str = yesterday.strftime('%d%m')
    print(yesterday_str)

    # Expected pattern for shipment files
    pattern = os.path.join(current_dir, '*export*.csv')
    shipment_files = glob.glob(pattern)
    print(shipment_files)

    # Check if shipment files are found
    if not shipment_files:
        print("No shipment files found.")
        return

    # Assuming you are processing only the first file found
    shipment_file = shipment_files[0]
    print(f"Found shipment file: {shipment_file}")

    # Define the new file name with yesterday's date
    new_file_name = f"{yesterday_str}.csv"
    new_file_path = os.path.join(destination_dir, new_file_name)

    os.rename(shipment_file, new_file_path)
    print(f"Renamed file: {shipment_file} to {new_file_path}")



def collate_trip(destination_dir, destination_complement_dir):
    print('collate trip')
    current_dir = DOWNLOAD_FOLDER_TMS

    now = datetime.now()
    date_str = now.strftime('%Y%m')

    pattern = os.path.join(current_dir, '*Trip*.csv')
    trip_files = glob.glob(pattern)

    # Assuming you are processing only the first file found
    trip_file = trip_files[-1]
    trip_file_complement = trip_files[0]

    # Define the new file name
    new_file_name = f"{date_str}.csv"
    new_file_path = os.path.join(destination_dir, new_file_name)

    new_file_name_complement = f"{date_str} bù.csv"
    new_file_path_complement = os.path.join(destination_complement_dir, new_file_name_complement)

    # Check if the file already exists in the destination directory
    if os.path.exists(new_file_path):
        print(f"File already exists. Replacing: {new_file_path}")
        os.replace(trip_file, new_file_path)  # Overwrite the file
    else:
        print(f"File does not exist. Renaming to: {new_file_path}")
        os.rename(trip_file, new_file_path)  # Rename the file

    if os.path.exists(new_file_path_complement):
        print(f"File already exists. Replacing: {new_file_path_complement}")
        os.replace(trip_file_complement, new_file_path_complement)  # Overwrite the file
    else:
        print(f"File does not exist. Renaming to: {new_file_path_complement}")
        os.rename(trip_file_complement, new_file_path_complement)  # Rename the file

    print(f"Operation complete: {trip_file_complement} -> {new_file_path_complement}")


def collate_today_tms(current_dir, destination_dir):
    # Find a CSV file in the current directory
    csv_files = [f for f in os.listdir(current_dir) if f.endswith('.csv')]
    if not csv_files:
        raise FileNotFoundError("No CSV files found in the current directory.")

    # Use the first CSV file found
    original_file = csv_files[0]
    original_path = os.path.join(current_dir, original_file)

    # Copy the original file and rename the copy to 'today.csv'
    renamed_path = os.path.join(current_dir, 'today.csv')
    shutil.copy2(original_path, renamed_path)

    # Move the original file to the destination directory
    shutil.move(original_path, os.path.join(destination_dir, original_file))

    print(f"'{original_file}' has been copied and renamed to 'today.csv', and the original has been moved to '{destination_dir}'.")
