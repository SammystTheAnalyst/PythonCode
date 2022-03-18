from bs4 import BeautifulSoup
import requests

url = 'https://ng.indeed.com/jobs?q=customer%20service&l&vjk=1c0193efff1ca105'

payload = {
    'q': 'customer service',
    'start': 0,
}

for start in range(0, 70, 10):
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


    import pandas as pd
    Indeed_Customer_ServiceJobs = pd.DataFrame({"Job Title": job_title, "Company Name": company_name, "Salary": salary, "Published date": published_date, "Location": location}, index=[0])
    Indeed_Customer_ServiceJobs.to_csv('Indeed_Customer_ServiceJobs.csv', index=False, encoding='utf-8', mode='a')


#    print(f'''
#    Job Title: {job_title}
#    Company Name: {company_name}
#    salary: {salary}
#    Published Date: {published_date}
#    Location: {location}
#    ''')
