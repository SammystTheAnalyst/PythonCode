from bs4 import BeautifulSoup
import requests
from csv import writer

url = 'https://ng.indeed.com/jobs?q=customer%20service&l&vjk=1c0193efff1ca105'

payload = {
    'q': 'customer service',
    'start': 0,
}

all_rows = []

for start in range(0, 101, 10):
    print('\n---- start:', start, '---\n')
    payload['start'] = start
    response = requests.get(url, params=payload)

    html_text = response.text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('div', class_='job_seen_beacon')
    for job in jobs:
        job_title = job.find('h2', class_='jobTitle').text.strip()
        company_name = job.find('span', class_='companyName').text.strip()
        salary = job.find('div', class_='salary-snippet')
        if salary:
            salary = salary.text.strip()
        published_date = job.find('span', class_='date').text.strip()
        location = job.find('div', class_='companyLocation').text.strip()

        row = [job_title, company_name, salary, published_date, location]
        all_rows.append(row)

        # print(f'''
        # Job Title: {job_title}
        # Company Name: {company_name}
        # Salary: {salary}
        # Published Date: {published_date}
        # Location: {location}
        # ''')

        with open('output_1.csv', 'w', encoding='utf8') as f:
            csv_writer = writer(f)
            headers = ["Job Title", "Company Name", "Salary", "Published Date", "Location"]
            csv_writer.writerow(headers)
            csv_writer.writerows(all_rows)



