import os
from download_images import download_images


def folder_create(images, base_url=None):
    try:
        folder_name = input("Enter folder name:")
    except EOFError:
        print("No folder name entered.")
        return

    try:
        os.makedirs(folder_name, exist_ok=True)
    except OSError as exc:
        print(f"Could not create folder: {exc}")
        return

    download_images(images, folder_name, base_url=base_url)