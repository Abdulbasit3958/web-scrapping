# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

# website = 'https://www.adamchoi.co.uk/overs/detailed'
# # Set the path to your ChromeDriver executable as a raw string
# chrome_driver_path = r'C:\Users\SWPC-378\Downloads\chromedriver-win64\chromedriver.exe'
# service = Service(executable_path=chrome_driver_path)
# driver = webdriver.Chrome(service=service)
# driver.get(website)



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--ignore-ssl-errors=yes')
chrome_options.add_argument('--ignore-certificate-errors')

service = Service(executable_path=r'C:\Users\SWPC-378\Downloads\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get('https://www.adamchoi.co.uk/overs/detailed')
