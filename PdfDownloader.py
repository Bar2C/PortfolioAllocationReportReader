import requests
import os
from bs4 import BeautifulSoup

def pdf_downloader(url, directory):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    files = doc.find_all(string=lambda string: ".pdf" in string)
    if len(files) > 1:
        parent = files[1].parent
    else:
        parent = files[0].parent
    href_value = parent['href']

    url1 = "https://www.kap.org.tr" + href_value
    response = requests.get(url1)

    # Check if the request was successful
    if response.status_code == 200:
        file_name = parent.text
        file_path = os.path.join(directory, file_name)

        # Save the PDF file to the specified directory
        with open(file_path, 'wb') as file:
            file.write(response.content)

        print(f"PDF file '{file_name}' downloaded successfully to '{file_path}'.")
        return file_path  # Return the file path
    else:
        print("Failed to download the PDF file.")
        return None
