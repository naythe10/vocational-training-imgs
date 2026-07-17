from bs4 import BeautifulSoup
import requests
import os
import download_images
import folder_create

def main(url):
    #get response from target url
    r = requests.get(url)

    #create beautiful soup instance
    soup = BeautifulSoup(r.text, 'html-parser')

    #getting all images
    images = soup.find_all('img')

    folder_create(images)


if __name__ == "__main__":
    url = input("Enter URL: ")
    main(url)
