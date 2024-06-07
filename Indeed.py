import time
from selenium import webdriver
import csv
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import re

def convert_relative_date(text):
    today = datetime.now()
    if 'today' in text.lower():
        return today.strftime('%d-%m-%Y')
    elif 'just posted' in text.lower():
        return today.strftime('%d-%m-%Y')
    else:
        numbers = re.findall(r'\d+', text)
        if numbers:
            days_ago = int(numbers[0])
            date = today - timedelta(days=days_ago)
            return date.strftime('%d-%m-%Y')
        else:
            return 'N/A'

query = input("Enter job query:")
location = input("Enter job location:")
num_pages = int(input("Number of pages:"))
start_list = [page * 10 for page in range(num_pages)]
base_url = 'https://ae.indeed.com'

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

for start in start_list:
    url = base_url + f'/jobs?q={query}&l={location}&start={start}'
    driver.execute_script(f"window.open('{url}', 'tab{start}');")
    time.sleep(1)
    if (start + 10) % 30 == 0:  # Check if 30 pages have been processed
        print(f"Taking a 10-second break after processing {start + 10} pages.")
        time.sleep(5)  # Sleep for 5 seconds

with open(f'{query}_{location}_job_results.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Job Title', 'Company', 'Location', 'Job Link', 'Salary', 'Date Posted'])
    for start in start_list:
        driver.switch_to.window(f'tab{start}')
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        items = soup.find_all('td', {'class': 'resultContent'})

        for job in items:
            s_link = job.find('a')['href'] if job.find('a') else 'N/A'
            job_title_element = job.find('h2', class_='jobTitle')
            job_title = job_title_element.text.strip() if job_title_element else 'N/A'
            company_element = job.select_one('span.css-1x7z1ps.eu4oa1w0')
            company = company_element.text.strip() if company_element else 'N/A'
            location_elements = job.select('div.css-t4u72d.eu4oa1w0')
            location_parts = [elem.text.strip() for elem in location_elements]
            job_location = ' '.join(location_parts) if location_elements else 'N/A'
            salary_element = job.find('div', class_='metadata salary-snippet-container') or job.find('div', class_='metadata estimated-salary-container')
            salary = salary_element.text.strip() if salary_element else 'N/A'
            date_element = job.find('span', class_='date')
            date_text = date_element.text.strip() if date_element else 'N/A'
            date_posted = convert_relative_date(date_text)
            job_link = f"{base_url}{s_link}" if s_link != 'N/A' else 'N/A'

            writer.writerow([job_title, company, job_location, job_link, salary, date_posted])

        driver.close()

driver.quit()
