import httpx
from selectolax.parser import HTMLParser
import time
import csv
from datetime import datetime, timedelta
import re
from urllib.parse import urljoin

def get_html(baseurl, page):
    headers= {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    
    resp = httpx.get(baseurl + str(page), headers=headers, follow_redirects=True)
    html = HTMLParser(resp.text)

    return html 

def extract_text(html, sel):
    try:
        return html.css_first(sel).text().strip().replace('\n', ' ').replace('\t', ' ')
    except AttributeError:
        return None

def convert_relative_date(text):
    if text == 'Yesterday':
        return (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    match = re.search(r'(\d+) days ago', text)
    if match:
        days_ago = int(match.group(1))
        return (datetime.now() - timedelta(days=days_ago)).strftime('%Y-%m-%d')
    return datetime.now().strftime('%Y-%m-%d')

def parse_page(html, baseurl, page):    
    jobs = html.css("li.has-pointer-d")
    for job in jobs: 
        job_link = job.css_first('a[data-js-aid="jobID"]')
        job_url = urljoin(baseurl, job_link.attributes['href']) if job_link else None
        role = {
            "Name": extract_text(job, ".jb-title.m0.t-large"),
            "Company": extract_text(job, ".jb-company-loc.t-small .jb-company"),
            "Description": extract_text(job, ".jb-descr.m10t.t-small"),
            "Date Posted": convert_relative_date(extract_text(job, ".jb-date.col.p0x.t-xsmall.t-mute")),
            "Salary": extract_text(job, ".p0.m10r.jb-label-salary"),
            "Job ID Link": job_url
        }
        yield role 

def main():
    baseurl = "https://www.bayt.com/en/uae/jobs/data-jobs/?page="
    filename = "main.csv"

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        headers = ["Name", "Company", "Description", "Date Posted", "Salary", "Job ID Link"]
        writer.writerow(headers)

        for x in range(1, 2):
            print(f"Generating page: {x}")
            html = get_html(baseurl, x)
            
            data = parse_page(html, baseurl, x)
            for role in data:
                writer.writerow([role["Name"], role["Company"], role["Description"], role["Date Posted"], role["Salary"], role["Job ID Link"]])
            
            time.sleep(3)

    print(f"Data written to {filename}")

if __name__ == "__main__":
    main()
