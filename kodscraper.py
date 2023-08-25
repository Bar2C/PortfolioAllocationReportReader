import requests
from bs4 import BeautifulSoup

def scrape_contents_from_url(url):
    # Send a GET request to the URL
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the HTML content of the webpage using Beautiful Soup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all div elements with the specified class
        div_elements = soup.find_all('div', class_='comp-cell _04 vtable')

        if div_elements:
            try:
                with open('kodfinal.txt', 'w') as file:
                    for div_element in div_elements:
                        # Extract the text content within each div element
                        content = div_element.get_text(strip=True)  # Get the text content and remove leading/trailing whitespace
                        values = [value.strip() for value in content.split(', ')]

                        # Write each value on a separate line in the file
                        for value in values:
                            file.write(value + '\n')
                            file.write(value + '.E' + '\n')
                print("Data written to kodfinal.txt.")
            except Exception as e:
                print(f"Error writing to file: {e}")
        else:
            print("No matching content found in the specified URL.")
    else:
        print(f"Failed to fetch the webpage. Status Code: {response.status_code}")

# Replace 'your_url_here' with the actual URL where the content is located
scrape_contents_from_url('https://www.kap.org.tr/tr/bist-sirketler')
