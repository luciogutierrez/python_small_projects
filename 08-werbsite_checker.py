import csv
import requests

from fake_useragent import UserAgent
from http import HTTPStatus

def get_websits(csv_path: str):
    websites: list[str] = []
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if 'https://' not in row[1]:
                websites.append(f'https://{row[1]}')
            else:
                websites.append(row[1])
        return websites

#print(get_websits('08-websites.csv'))

def get_user_agent() -> str:
    ua = UserAgent()
    return ua.edge

#print(get_user_agent())

def get_status_description(status_code: int) -> str:
    for value in HTTPStatus:
        if value == status_code:
            description: str = f'({value} {value.name}) {value.description}'
            return description
    
    return '(???) Unknown status code...'

#print(HTTPStatus.BAD_REQUEST.name)
#print(HTTPStatus.BAD_REQUEST.value)

def check_wesite(website:str, user_agent):
    try:
        code: int = requests.get(website, headers={'User-Agent': user_agent}).status_code
        print(website, get_status_description(code))
    except Exception:
        print(f'**Could not get insformation for website: "{website}"')

def main():
    sites:list[str] = get_websits('08-websites.csv')
    user_agant: str = get_user_agent()

    for site in sites: 
        check_wesite(site, user_agant)

if __name__ == '__main__':
    main()


