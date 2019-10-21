import requests
from pprint import pprint

from bs4 import BeautifulSoup as bs

##### Lанные с HeadHunter
#Отфильтровать ЗП по максимальной не получилось, поскольку почему-то когда данные добавляются в список вместо пробелов отображаются
#\ха, на которые не делается replace


headers = {'accept': '*/*','user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}



base_link='https://hh.ru/search/vacancy?area=1&text=Python&page='


def hh_parse(base_link, headers):

    m = 0
    for n in range(3):

        job = []
        session = requests.Session()
        request = session.get(base_link + str(m), headers=headers)
        soup = bs(request.content, 'html.parser')
        divs = soup.find_all('div', attrs={'data-qa': 'vacancy-serp__vacancy'})
        for div in divs:
            title = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'}).text
            href = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'})['href']
            company = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-employer'}).text
            salary = div.find('div', attrs={'data-qa': 'vacancy-serp__vacancy-compensation'})

            if not salary:
                salary = 0
            else:
                salary = salary.text.replace(' ', '')
            job.append({'title': title, 'href': href, 'company': company, 'salary': salary})
        m +=1
    return job

pprint(hh_parse(base_link, headers))

















