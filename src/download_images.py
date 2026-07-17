from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import requests

def download_images(images, folder_name):
    count = 0
    for i, image in enumerate(images):

        #Find image src url, using these levels => 1)data-srcset 2)data-src 3)data-fallback-src 4)src
        try:
            image_link = image['data-srcset']
        except:
            try:
                image_link = image['data-src']
            except:
                try:
                    image_link = image['data-fallback-src']
                except:
                    try:
                        image_src = image['src']
                    except:
                        pass

        #Decode obtained link
        try:
            r = requests.get(image_link).content
            try:
                r = str(r, 'utf-8')
            except UnicodeDecodeError:
                with open(f"./{folder_name}/images{i+1}.jpg", "wb+") as f:
                    f.write(r)
                count += 1
        except:
            pass

        #Image counter
        if count == len(images):
            print("All images have been downloaded.")
        else:
            print(f"Downloaded {count} out of {len(images)} images.")