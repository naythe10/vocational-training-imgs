import os
from urllib.parse import urljoin, urlparse
import requests


def extract_image_url(image, base_url=None):
    for key in ("data-srcset", "srcset", "data-src", "data-fallback-src", "src"):
        value = image.get(key)
        if value:
            if key in {"data-srcset", "srcset"}:
                value = value.split(",")[0].strip().split()[0]
            if base_url:
                return urljoin(base_url, value)
            return value
    return None


def download_images(images, folder_name, base_url=None):
    os.makedirs(folder_name, exist_ok=True)
    successful_downloads = 0

    for i, image in enumerate(images, start=1):
        image_link = extract_image_url(image, base_url)
        if not image_link or image_link.startswith("#"):
            continue

        try:
            response = requests.get(image_link, timeout=20)
            response.raise_for_status()

            extension = os.path.splitext(urlparse(image_link).path)[1] or ".jpg"
            file_path = os.path.join(folder_name, f"image{i}{extension}")

            with open(file_path, "wb") as file_handle:
                file_handle.write(response.content)

            successful_downloads += 1
            print(f"Downloaded {successful_downloads} out of {len(images)} images.")
        except requests.RequestException as exc:
            print(f"Failed to download image {i}: {exc}")

    if successful_downloads == len(images):
        print("All images have been downloaded.")