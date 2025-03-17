from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from constants.constant import DOWNLOAD_FOLDER_SOS, DOWNLOAD_FOLDER_TMS




def initialize_driver(web):
    if web == 'sos':
        download_folder = DOWNLOAD_FOLDER_SOS  
    elif web == 'tms':
        download_folder = DOWNLOAD_FOLDER_TMS

    # Set up Chrome options
    chrome_driver = r"D:\sendo\Code\chromedriver-win64\chromedriver-win64\chromedriver.exe"
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Start the browser maximized
    chrome_options.add_argument('--disable-gpu')  # Disable GPU (useful for certain systems)
    chrome_options.add_argument('--no-sandbox')  # No sandbox mode (useful for some environments)
    chrome_options.add_argument('--disable-dev-shm-usage')  # Prevent shared memory usage issues

    # Configure download preferences
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_folder,  # Automatically save files to this folder
        "download.prompt_for_download": False,          # Disable the file destination popup
        "download.directory_upgrade": True,             # Automatically overwrite existing files
        "plugins.always_open_pdf_externally": True,     # PDFs should be downloaded, not opened in the browser
        "safebrowsing.enabled": True,                   # Enable safe browsing
        "profile.default_content_setting_values.automatic_downloads": 1  # Allow multiple downloads
    })

    # Use Service to specify the ChromeDriver path
    service = Service(chrome_driver)

    # Initialize the WebDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    print("Driver initialized.")

    # # Set browser zoom to 80%
    # if web == 'tms':
    #     driver.execute_cdp_cmd("Emulation.setDeviceMetricsOverride", {
    #         "width": 1920,   # Full screen width
    #         "height": 1080,  # Full screen height
    #         "deviceScaleFactor": 1,
    #         "mobile": False,
    #         "scale": 0.8     # Set the zoom scale to 80%
    #     })


    return driver