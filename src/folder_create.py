import os
import download_images

def folder_create(images):
    cwd = os.chdir('..')
    try:
        folder_name = input("Enter folder name:")
        os.mkdir(folder_name)
    except:
        print('Folder already exist, try another name!')
        folder_create()
    download_images(images, folder_name)