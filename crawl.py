import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_image(url, folder):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(os.path.join(folder, url.split("/")[-1]), "wb") as f:
                f.write(response.content)
                print(f"Downloaded: {url}")
    except Exception as e:
        print(f"Failed to download {url}. Error: {str(e)}")

def scrape_images(url, folder):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            img_tags = soup.find_all("img")
            for img_tag in img_tags:
                img_url = img_tag.get("src")
                if img_url:
                    img_url = urljoin(url, img_url)
                    download_image(img_url, folder)
    except Exception as e:
        print(f"Failed to scrape {url}. Error: {str(e)}")

def main():
    url = input("Enter the URL of the website: ")
    folder = "data"
    if not os.path.exists(folder):
        os.makedirs(folder)
    scrape_images(url, folder)

if __name__ == "__main__":
    main()
