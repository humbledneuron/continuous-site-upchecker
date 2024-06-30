from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import messagebox
import time
import winsound

def check_site(driver, url):
    try:
        # Open or refresh the website
        driver.get(url)
        
        # Wait until the statusup element is present
        wait = WebDriverWait(driver, 5)
        statusup = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "statusup")))
        
        status = statusup.text.strip().split()[2]
        
        if status == 'UP':
            return True
        else:
            return False
    except Exception as e:
        # print(f"Error: {e}")
        return False

def main():
    site_on_checker = 'https://www.isitdownrightnow.com/'
    site_url = 'transfers.dse.telangana.gov.in' #.capitalize()
    site_url = site_on_checker + site_url + '.html'
    print(site_url)
    
    # Initialize Chrome WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless') 
    service = Service("/home/pr3cash/Desktop/py_learn/twt/selnium/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)

    try:
        while True:
            if check_site(driver, site_url):
                print(f"{site_url} is up.")
                winsound.Beep(500, 5000)
                messagebox.showwarning("Success", f"The site {site_url} is back online.")
                break
            else:
                print(f"{site_url} is down.")
            time.sleep(300)  # Check every 300 seconds or 5 mins
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
