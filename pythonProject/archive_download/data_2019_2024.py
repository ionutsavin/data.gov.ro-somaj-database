import requests
import os

romanian_month_mapping = {
    "Ianuarie": 1,
    "Februarie": 2,
    "Martie": 3,
    "Aprilie": 4,
    "Mai": 5,
    "Iunie": 6,
    "Iulie": 7,
    "August": 8,
    "Septembrie": 9,
    "Octombrie": 10,
    "Noiembrie": 11,
    "Decembrie": 12
}

criteriu_mapping = {
    "rata": 1,
    "medii": 2,
    "educatie": 3,
    "varste": 4,
}


def get_dataset_id(month_name, year):
    if year == 2021 and month_name == "Decembrie":
        return "somajul-inregistrat-dcembrie-2021"
    elif year == 2020 and month_name == "Noiembrie":
        return "somaj-noiembrie-2020"
    elif year == 2020 and month_name == "Mai":
        return "somajul-inregistrat-mai2020"
    else:
        return f"somajul-inregistrat-{month_name.lower()}-{year}"


start_month = "Martie"
start_year = 2024
end_month = "Ianuarie"
end_year = 2019


def download_files():
    current_year = start_year
    while current_year >= end_year:
        for month_name in romanian_month_mapping.keys():
            dataset_id = get_dataset_id(month_name, current_year)
            url = f"https://data.gov.ro/api/3/action/package_show?id={dataset_id}"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                resources = data.get('result', {}).get('resources', [])

                year_directory = f"arhiva_somaj/{current_year}"
                month_directory = os.path.join(year_directory, month_name)
                os.makedirs(month_directory, exist_ok=True)

                for resource in resources:
                    resource_url = resource.get('url', '')
                    url_type = resource.get('url_type', '')

                    if resource_url.endswith('.csv') and url_type == 'upload':
                        index = 0
                        if "rata" in resource_url:
                            index = criteriu_mapping["rata"]
                        elif "medii" in resource_url:
                            index = criteriu_mapping["medii"]
                        elif "educatie" in resource_url or "nivel-ed" in resource_url:
                            index = criteriu_mapping["educatie"]
                        elif "varste" in resource_url:
                            index = criteriu_mapping["varste"]

                        if index > 0:
                            file_response = requests.get(resource_url)

                            if file_response.status_code == 200:
                                file_name = f"somajul_inregistrat_{month_name.lower()}_{current_year}_{index}.csv"
                                file_path = os.path.join(month_directory, file_name)

                                with open(file_path, 'wb') as f:
                                    f.write(file_response.content)
                                print(f"File {month_name} {current_year} {index} downloaded successfully.")
                            else:
                                print(f"Failed to download file from {resource_url}")
            else:
                print(f"Failed to fetch the dataset for {month_name} {current_year}.")

        current_year -= 1
