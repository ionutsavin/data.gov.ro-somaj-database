import requests
from bs4 import BeautifulSoup
import os


def download_files(data_url, data_year, months):
    response = requests.get(data_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        download_links = soup.find_all('a', {'class': 'resource-url-analytics'})

        if download_links:
            month_index = 0

            for idx, download_link in enumerate(download_links, 1):
                download_url = download_link['href']
                file_response = requests.get(download_url)
                month_name = months[month_index]
                file_idx = idx % 4 if idx % 4 != 0 else 4

                if file_response.status_code == 200:
                    directory_name = f"arhiva_somaj/{data_year}/{month_name}"
                    os.makedirs(directory_name, exist_ok=True)

                    file_path = f"{directory_name}/somajul_inregistrat_{month_name.lower()}_{data_year}_{file_idx}.csv"
                    with open(file_path, 'wb') as f:
                        f.write(file_response.content)
                    print(f"File {month_name} {data_year} {file_idx} downloaded successfully.")

                    if idx % 4 == 0:
                        month_index = (month_index + 1) % len(months)
                else:
                    print(f"Failed to download file {month_name} {data_year} {file_idx}.")
        else:
            print("No download links found.")
    else:
        print("Failed to fetch the page.")
