from bs4 import BeautifulSoup
import requests
import os
from folder_create import folder_create

def main(url):
    #get response from target url
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36'
    }

    r = requests.get(url, headers= headers)

    #create beautiful soup instance
    soup = BeautifulSoup(r.text, 'html.parser')

    #getting all images
    images = soup.find_all('img')

    folder_create(images, base_url=url)


if __name__ == "__main__":
    url = input("Enter URL: ")
    main(url)
