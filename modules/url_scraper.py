import requests
from bs4 import BeautifulSoup

email_list = []


def scraper(formated_url):
    try:
        response = requests.get(formated_url, timeout=10)
        response.raise_for_status()  # Raises an error for non-200 status codes
        soup = BeautifulSoup(response.text, 'html.parser')

        emails = soup.find_all('a', class_='email')
        for i in emails:
            i_text = i.get_text()
            email_list.append(i_text)

        #print(f'URL: {formated_url}\nStatus: {response.status_code}\n \n' + '\n'.join(email_list))
    except requests.exceptions.RequestException as e:
        print(f'Error: Unable to reach the website: {formated_url}')
        print(e)


